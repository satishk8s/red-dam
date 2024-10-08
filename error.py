Test Event Name
dam

Response
{
  "errorMessage": "Only base64 data is allowed",
  "errorType": "Error",
  "requestId": "21379561-8041-48e3-84a6-f6865b9c2723",
  "stackTrace": [
    "  File \"/var/task/lambda_function.py\", line 26, in lambda_handler\n    decoded_data = base64.b64decode(cw_data, validate=True)\n",
    "  File \"/var/lang/lib/python3.12/base64.py\", line 88, in b64decode\n    return binascii.a2b_base64(s, strict_mode=validate)\n"
  ]
}

Function Logs
START RequestId: 21379561-8041-48e3-84a6-f6865b9c2723 Version: $LATEST
LAMBDA_WARNING: Unhandled exception. The most likely cause is an issue in the function code. However, in rare cases, a Lambda runtime update can cause unexpected function behavior. For functions using managed runtimes, runtime updates can be triggered by a function change, or can be applied automatically. To determine if the runtime has been updated, check the runtime version in the INIT_START log entry. If this error correlates with a change in the runtime version, you may be able to mitigate this error by temporarily rolling back to the previous runtime version. For more information, see https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html
[ERROR] Error: Only base64 data is allowed
Traceback (most recent call last):
  File "/var/task/lambda_function.py", line 26, in lambda_handler
    decoded_data = base64.b64decode(cw_data, validate=True)
  File "/var/lang/lib/python3.12/base64.py", line 88, in b64decode
    return binascii.a2b_base64(s, strict_mode=validate)END RequestId: 21379561-8041-48e3-84a6-f6865b9c2723
REPORT RequestId: 21379561-8041-48e3-84a6-f6865b9c2723	Duration: 13.37 ms	Billed Duration: 14 ms	Memory Size: 128 MB	Max Memory Used: 81 MB	Init Duration: 551.05 ms

Request ID
21379561-8041-48e3-84a6-f6865b9c2723
