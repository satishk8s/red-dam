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

DYNAMODB_TABLE_NAME = "dam_user_filter"
S3_BUCKET_NAME = "dam-db-audit-logs"
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    '''
    Lambda function handler
    '''
    logger.info(f"Received event: {json.dumps(event)}")

    # Handle both gzipped and plain text CloudWatch Logs
    cw_data = event['awslogs']['data']
    decoded_data = base64.b64decode(cw_data, validate=True)
    
    try:
        # Try to decompress as GZIP
        cw_logs = gzip.GzipFile(fileobj=BytesIO(decoded_data)).read()
        log_events = json.loads(cw_logs)
    except gzip.BadGzipFile:
        # If not GZIP, assume it's plain JSON
        log_events = json.loads(decoded_data)

    logger.info(f"Decrypted event: {log_events}")

    # Get account ID from STS
    sts = boto3.client('sts')
    account_id = sts.get_caller_identity()['Account']

    dynamodb = boto3.resource('dynamodb')

    # Determine log stream
    log_stream = event.get('logStream', 'UnknownLogStream')  # Default value if logStream not present
    logger.info(f"Log Stream: {log_stream}")

    # Assume database name is derived from log_stream
    database_name = log_stream

    # Fetch users from DynamoDB
    key = {"dbName": database_name}
    db_users = get_dynamo_db_item(DYNAMODB_TABLE_NAME, key, dynamodb)
    logger.info(f"Users in database: {db_users}")

    # Check if log events exist
    if 'logEvents' in log_events:
        for log_event in log_events['logEvents']:
            message = log_event['message'].strip()
            logger.info(f"Processing log message: {message}")
            
            query_message = message.split('|')[1].strip()  # Extracting the username from the log message
            
            # Check if there are users in DynamoDB
            if 'Item' in db_users:
                if 'humanUsers' in db_users['Item']:
                    human_users = [user['S'] for user in db_users['Item']['humanUsers']['L']]
                    
                    if query_message in human_users:
                        dam_event = create_event(message, database_name, account_id)
                        filter_event(dam_event, known_user=True)
                    else:
                        logger.warning(f"User {query_message} is not in DynamoDB, treating as unknown user.")
                        dam_event = create_event(message, database_name, account_id)
                        filter_event(dam_event, known_user=False)
                else:
                    logger.warning("No human users found in DynamoDB, treating all users as unknown.")
                    dam_event = create_event(message, database_name, account_id)
                    filter_event(dam_event, known_user=False)
            else:
                logger.warning("No DynamoDB entry found for this database, treating all users as unknown.")
                dam_event = create_event(message, database_name, account_id)
                filter_event(dam_event, known_user=False)
    else:
        logger.error("No logEvents found in log data.")

def filter_event(dam_event, known_user):
    query = dam_event['query'].lower()
    logger.info(f"Query - {query}")
    push_event = 0

    # User-related queries
    user_related_queries = ["create user", "alter user", "drop user", "grant", "revoke", "rename user"]

    # Check if the query is user-related
    if any(q in query for q in user_related_queries):
        dam_event['queryType'] = "User Management"
        push_event = 1

    # Process the affected user from the query text
    if "create user" in query or "alter user" in query or "drop user" in query:
        affected_username = query.split(' ')[2] if len(query.split(' ')) > 2 else "unknown"
        dam_event['affectedUser'] = [affected_username]

    # Upload to S3 if it's a relevant event
    if push_event == 1:
        logger.info("User-related query found. Publishing to S3")
        upload_to_s3(dam_event, known_user)

def create_event(message, database_name, account_id):
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
    '''
    Function to parse and structure a log event message
    '''
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
    '''
    Uploads event to S3 bucket with folder structure db_name/year/month/day/
    '''
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

def get_dynamo_db_item(table_name, key, dynamodb=None):
    '''
    Get item from given DynamoDB table and key
    '''
    if dynamodb is None:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    try:
        response = table.get_item(Key=key)
        return response
    except Exception as e:
        logger.error(f"Failed to get item from DynamoDB: {e}")
        return {}
