Test Event Name
damtest

Response
{
  "errorMessage": "list index out of range",
  "errorType": "IndexError",
  "requestId": "26a112ec-8189-4f4a-80eb-dbce5b9d3a66",
  "stackTrace": [
    "  File \"/var/task/lambda_function.py\", line 65, in lambda_handler\n    dam_event = create_event(log_event, database_name, account_id)\n",
    "  File \"/var/task/lambda_function.py\", line 92, in create_event\n    audit_event = normalize_event(log_event['message'])\n",
    "  File \"/var/task/lambda_function.py\", line 114, in normalize_event\n    \"username\": audit_event[1],\n"
  ]
}

Function Logs
START RequestId: 26a112ec-8189-4f4a-80eb-dbce5b9d3a66 Version: $LATEST
event - {'awslogs': {'data': 'eyJsb2dFdmVudHMiOiBbeyJtZXNzYWdlIjogIjEwMXxzYXRpc2ggfCAgY3JlYXRlIHwgfDAgfHwwIHwgODgwIHwgdHlwZSAtIGxvY2F0aW9uLnNwYWNlIHx8IHdyaXRlIHwgZW5kX3RpbWV8fHdoaXRlIDB8fGNoYW5uZWwifV19'}}
decrypted event - {'logEvents': [{'message': '101|satish |  create | |0 ||0 | 880 | type - location.space || write | end_time||white 0||channel'}]}
Log Stream: UnknownLogStream
users in database - {'ResponseMetadata': {'RequestId': '754H9TKE9G1CUBCCRETN3R7MUNVV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200, 'HTTPHeaders': {'server': 'Server', 'date': 'Thu, 03 Oct 2024 13:06:09 GMT', 'content-type': 'application/x-amz-json-1.0', 'content-length': '2', 'connection': 'keep-alive', 'x-amzn-requestid': '754H9TKE9G1CUBCCRETN3R7MUNVV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '2745614147'}, 'RetryAttempts': 0}}
No DynamoDB entry found for database, treating all users as unknown.
LAMBDA_WARNING: Unhandled exception. The most likely cause is an issue in the function code. However, in rare cases, a Lambda runtime update can cause unexpected function behavior. For functions using managed runtimes, runtime updates can be triggered by a function change, or can be applied automatically. To determine if the runtime has been updated, check the runtime version in the INIT_START log entry. If this error correlates with a change in the runtime version, you may be able to mitigate this error by temporarily rolling back to the previous runtime version. For more information, see https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html
[ERROR] IndexError: list index out of range
Traceback (most recent call last):
  File "/var/task/lambda_function.py", line 65, in lambda_handler
    dam_event = create_event(log_event, database_name, account_id)
  File "/var/task/lambda_function.py", line 92, in create_event
    audit_event = normalize_event(log_event['message'])
  File "/var/task/lambda_function.py", line 114, in normalize_event
    "username": audit_event[1],END RequestId: 26a112ec-8189-4f4a-80eb-dbce5b9d3a66
REPORT RequestId: 26a112ec-8189-4f4a-80eb-dbce5b9d3a66	Duration: 1874.20 ms	Billed Duration: 1875 ms	Memory Size: 128 MB	Max Memory Used: 88 MB

Request ID
26a112ec-8189-4f4a-80eb-dbce5b9d3a66
