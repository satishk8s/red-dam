import os
import json
import base64
import boto3
from datetime import datetime
from io import BytesIO
import gzip
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

DYNAMODB_TABLE_NAME = "dam_user_filter"  # Your DynamoDB table name
S3_BUCKET_NAME = "redshift-uppin"  # Your S3 bucket name
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    """
    Lambda function handler.
    Processes CloudWatch Logs data, extracts usernames, checks against DynamoDB,
    and uploads relevant events to S3.
    """
    logger.info(f"Received event: {json.dumps(event)}")

    # Check for base64 encoding
    cw_data = event['awslogs']['data']
    
    if not is_base64(cw_data):
        logger.error("Provided data is not base64-encoded")
        return {"error": "Provided data is not base64-encoded"}

    try:
        decoded_data = base64.b64decode(cw_data, validate=True)
    except Exception as e:
        logger.error(f"Error decoding base64 data: {str(e)}")
        return {"error": f"Error decoding base64 data: {str(e)}"}

    # Attempt to decompress GZIP data
    log_events = decode_and_decompress(decoded_data)

    if log_events is None:
        return {"error": "Failed to parse log events."}

    # Get account ID from STS
    sts = boto3.client('sts')
    account_id = sts.get_caller_identity()['Account']

    # Determine log stream
    log_stream = event.get('logStream', 'UnknownLogStream')
    logger.info(f"Log Stream: {log_stream}")

    # Assume database name is derived from log_stream
    database_name = log_stream

    # Fetch users from DynamoDB
    db_users = get_dynamo_db_item(DYNAMODB_TABLE_NAME, {"dbName": database_name})
    logger.info(f"Users in database: {db_users}")

    # Process log events
    process_log_events(log_events, database_name, account_id, db_users)

def decode_and_decompress(decoded_data):
    """
    Attempt to decompress data, trying GZIP first.
    If that fails, assume plain JSON.
    """
    try:
        # Try to decompress as GZIP
        with gzip.GzipFile(fileobj=BytesIO(decoded_data)) as f:
            cw_logs = f.read()
        return json.loads(cw_logs)
    except gzip.BadGzipFile:
        # If not GZIP, assume it's plain text
        return {'logEvents': [{'message': decoded_data.decode('utf-8')}]}
    except Exception as e:
        logger.error(f"Error parsing JSON data: {str(e)}")
        return None

def process_log_events(log_events, database_name, account_id, db_users):
    """
    Process each log event, checking for known users and filtering events.
    """
    if 'logEvents' not in log_events:
        logger.error("No logEvents found in log data.")
        return

    human_users = []
    if 'Item' in db_users and 'humanUsers' in db_users['Item']:
        human_users = [user['S'] for user in db_users['Item']['humanUsers']['L']]
    else:
        logger.warning("No human users found in DynamoDB, treating all users as unknown.")

    for log_event in log_events['logEvents']:
        message = log_event['message'].strip()
        logger.info(f"Processing log message: {message}")

        # Ensure we don't split beyond available indices
        parts = message.split('|')
        if len(parts) > 1:
            query_message = parts[1].strip()  # Extracting the username from the log message
        else:
            logger.warning("Log message format is incorrect, skipping.")
            continue

        known_user = query_message in human_users
        dam_event = create_event(message, database_name, account_id)
        filter_event(dam_event, known_user)

def is_base64(data):
    """
    Check if the provided data is valid base64-encoded.
    """
    try:
        base64.b64decode(data, validate=True)
        return True
    except Exception:
        return False

def filter_event(dam_event, known_user):
    """
    Filter event based on query type and upload to S3 if relevant.
    """
    query = dam_event['query'].lower()
    logger.info(f"Query - {query}")

    # User-related queries
    user_related_queries = ["create user", "alter user", "drop user", "grant", "revoke", "rename user"]

    # Check if the query is user-related
    if any(q in query for q in user_related_queries):
        dam_event['queryType'] = "User Management"
        affected_username = query.split(' ')[2] if len(query.split(' ')) > 2 else "unknown"
        dam_event['affectedUser'] = [affected_username]

        # Upload to S3 if it's a relevant event
        logger.info("User-related query found. Publishing to S3")
        upload_to_s3(dam_event, known_user)

def create_event(message, database_name, account_id):
    """
    Create an event from the log message.
    """
    audit_event = normalize_event(message)
    
    dam_event = {
        "region": os.environ['AWS_REGION'],
        "databaseName": database_name,
        "accountId": account_id,
        "messageId": f"{datetime.now().timestamp()}"  # Generating a unique message ID
    }
    dam_event.update(audit_event)

    logger.info(f"Created event: {json.dumps(dam_event)}")
    
    return dam_event

def normalize_event(message):
    """
    Function to parse and structure a log event message.
    """
    audit_event = message.split('|')
    
    dam_event = {
        "timestamp": audit_event[9] if len(audit_event) > 9 else "unknown",
        "username": audit_event[1] if len(audit_event) > 1 else "unknown",
        "connectionId": audit_event[2] if len(audit_event) > 2 else "unknown",
        "database": audit_event[3] if len(audit_event) > 3 else "unknown",
        "query": audit_event[4] if len(audit_event) > 4 else "unknown",
        "originalEvent": message
    }
    logger.info(f"Parsed event - {dam_event}")
    return dam_event

def upload_to_s3(dam_event, known_user):
    """
    Uploads event to S3 bucket with folder structure db_name/year/month/day/.
    """
    try:
        now = datetime.now()
        year = now.strftime('%Y')
        month = now.strftime('%m')
        day = now.strftime('%d')
        timestamp = now.strftime('%H-%M-%S')
        
        db_name = dam_event['databaseName']
        
        folder = 'unknown_users' if not known_user else ''
        s3_key = f"{db_name}/{folder}/{year}/{month}/{day}/{timestamp}_{dam_event['messageId']}.json"
        
        s3_client.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=s3_key,
            Body=json.dumps(dam_event, default=str)
        )
        logger.info(f"Successfully uploaded {s3_key} to S3.")
    except Exception as e:
        logger.error(f'Error saving event to S3: {str(e)}')

def get_dynamo_db_item(table_name, key):
    """
    Get item from given DynamoDB table and key.
    """
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    try:
        response = table.get_item(Key=key)
        return response
    except Exception as e:
        logger.error(f"Failed to get item from DynamoDB: {e}")
        return {}
