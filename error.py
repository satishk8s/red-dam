Test Event Name
damtest

Response
{
  "errorMessage": "'logStream'",
  "errorType": "KeyError",
  "requestId": "4bc32e4b-fab6-4562-9eee-836f6ecaee74",
  "stackTrace": [
    "  File \"/var/task/lambda_function.py\", line 41, in lambda_handler\n    database_name = log_events['logStream']\n"
  ]
}

Function Logs
START RequestId: 4bc32e4b-fab6-4562-9eee-836f6ecaee74 Version: $LATEST
event - {'awslogs': {'data': 'eyJsb2dFdmVudHMiOiBbeyJtZXNzYWdlIjogIjEwMXxzYXRpc2ggfCAgY3JlYXRlIHwgfDAgfHwwIHwgODgwIHwgdHlwZSAtIGxvY2F0aW9uLnNwYWNlIHx8IHdyaXRlIHwgZW5kX3RpbWV8fHdoaXRlIDB8fGNoYW5uZWwifV19'}}
decrypted event - {'logEvents': [{'message': '101|satish |  create | |0 ||0 | 880 | type - location.space || write | end_time||white 0||channel'}]}
LAMBDA_WARNING: Unhandled exception. The most likely cause is an issue in the function code. However, in rare cases, a Lambda runtime update can cause unexpected function behavior. For functions using managed runtimes, runtime updates can be triggered by a function change, or can be applied automatically. To determine if the runtime has been updated, check the runtime version in the INIT_START log entry. If this error correlates with a change in the runtime version, you may be able to mitigate this error by temporarily rolling back to the previous runtime version. For more information, see https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html
[ERROR] KeyError: 'logStream'
Traceback (most recent call last):
  File "/var/task/lambda_function.py", line 41, in lambda_handler
    database_name = log_events['logStream']END RequestId: 4bc32e4b-fab6-4562-9eee-836f6ecaee74
REPORT RequestId: 4bc32e4b-fab6-4562-9eee-836f6ecaee74	Duration: 1813.16 ms	Billed Duration: 1814 ms	Memory Size: 128 MB	Max Memory Used: 87 MB	Init Duration: 366.86 ms

Request ID
4bc32e4b-fab6-4562-9eee-836f6ecaee74
