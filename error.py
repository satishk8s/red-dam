Test Event Name
dam

Response
{
  "errorMessage": "list index out of range",
  "errorType": "IndexError",
  "requestId": "9177b00c-4219-4251-a9a8-4626566ee36d",
  "stackTrace": [
    "  File \"/var/task/lambda_function.py\", line 61, in lambda_handler\n    process_log_events(log_events, database_name, account_id, db_users)\n",
    "  File \"/var/task/lambda_function.py\", line 91, in process_log_events\n    query_message = message.split('|')[1].strip()  # Extracting the username from the log message\n"
  ]
}

Function Logs
START RequestId: 9177b00c-4219-4251-a9a8-4626566ee36d Version: $LATEST
LAMBDA_WARNING: Unhandled exception. The most likely cause is an issue in the function code. However, in rare cases, a Lambda runtime update can cause unexpected function behavior. For functions using managed runtimes, runtime updates can be triggered by a function change, or can be applied automatically. To determine if the runtime has been updated, check the runtime version in the INIT_START log entry. If this error correlates with a change in the runtime version, you may be able to mitigate this error by temporarily rolling back to the previous runtime version. For more information, see https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html
[ERROR] IndexError: list index out of range
Traceback (most recent call last):
  File "/var/task/lambda_function.py", line 61, in lambda_handler
    process_log_events(log_events, database_name, account_id, db_users)
  File "/var/task/lambda_function.py", line 91, in process_log_events
    query_message = message.split('|')[1].strip()  # Extracting the username from the log messageEND RequestId: 9177b00c-4219-4251-a9a8-4626566ee36d
REPORT RequestId: 9177b00c-4219-4251-a9a8-4626566ee36d	Duration: 1895.46 ms	Billed Duration: 1896 ms	Memory Size: 128 MB	Max Memory Used: 88 MB	Init Duration: 544.05 ms

Request ID
9177b00c-4219-4251-a9a8-4626566ee36d
