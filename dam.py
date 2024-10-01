import json
import boto3
import base64
from datetime import datetime

# Initialize the S3 client
s3_client = boto3.client('s3')

# Replace with your S3 bucket name
S3_BUCKET_NAME = 'your-s3-bucket-name'

def lambda_handler(event, context):
    # Iterate over CloudWatch log event batches
    for record in event['Records']:
        # Extract the CloudWatch log event data
        cloudwatch_logs = record['awslogs']['data']
        decoded_logs = base64.b64decode(cloudwatch_logs)
        logs = json.loads(decoded_logs)
        
        # Iterate over each log event
        for log_event in logs['logEvents']:
            message = log_event['message']
            # Process the log message as needed (in your case, it's the format provided)
            
            # Parse the user log data (e.g., pipe-separated values)
            log_data = message.split('|')
            
            # Example format: 107|pawantilokani | |create |0|0|0|9223372036854775807|1073742232|98382871|Tue, 10 Sep 2024 12:04:47:041
            log_entry = {
                "user_id": log_data[0],
                "username": log_data[1].strip(),
                "action": log_data[3],
                "timestamp": log_data[10]
            }
            
            # Create a filename based on the current timestamp and user
            timestamp = datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S')
            filename = f'redshift_logs/{log_entry["username"]}/{timestamp}.json'
            
            # Save the log entry to S3 as a JSON file
            s3_client.put_object(
                Bucket=S3_BUCKET_NAME,
                Key=filename,
                Body=json.dumps(log_entry),
                ContentType='application/json'
            )
            
            print(f'Successfully sent log entry for user {log_entry["username"]} to S3')

    return {
        'statusCode': 200,
        'body': json.dumps('Logs successfully processed and sent to S3')
    }
