Test Event Name
damtest

Response
{
  "errorMessage": "'id'",
  "errorType": "KeyError",
  "requestId": "6795fe66-02b7-4e64-98b5-1061b6d08b6d",
  "stackTrace": [
    "  File \"/var/task/lambda_function.py\", line 73, in lambda_handler\n    dam_event = create_event(log_event, database_name, account_id)\n",
    "  File \"/var/task/lambda_function.py\", line 108, in create_event\n    \"messageId\": log_event['id']\n"
  ]
}

Function Logs
START RequestId: 6795fe66-02b7-4e64-98b5-1061b6d08b6d Version: $LATEST
[WARNING]	2024-10-03T13:11:59.748Z	6795fe66-02b7-4e64-98b5-1061b6d08b6d	No DynamoDB entry found for this database, treating all users as unknown.
LAMBDA_WARNING: Unhandled exception. The most likely cause is an issue in the function code. However, in rare cases, a Lambda runtime update can cause unexpected function behavior. For functions using managed runtimes, runtime updates can be triggered by a function change, or can be applied automatically. To determine if the runtime has been updated, check the runtime version in the INIT_START log entry. If this error correlates with a change in the runtime version, you may be able to mitigate this error by temporarily rolling back to the previous runtime version. For more information, see https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html
[ERROR] KeyError: 'id'
Traceback (most recent call last):
  File "/var/task/lambda_function.py", line 73, in lambda_handler
    dam_event = create_event(log_event, database_name, account_id)
  File "/var/task/lambda_function.py", line 108, in create_event
    "messageId": log_event['id']END RequestId: 6795fe66-02b7-4e64-98b5-1061b6d08b6d
REPORT RequestId: 6795fe66-02b7-4e64-98b5-1061b6d08b6d	Duration: 2499.27 ms	Billed Duration: 2500 ms	Memory Size: 128 MB	Max Memory Used: 88 MB	Init Duration: 560.59 ms

Request ID
6795fe66-02b7-4e64-98b5-1061b6d08b6d
