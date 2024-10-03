Test Event Name
damtest

Response
{
  "errorMessage": "An error occurred (AccessDeniedException) when calling the GetItem operation: User: arn:aws:sts::137141637317:assumed-role/red-dam-role-b0q1toew/red-dam is not authorized to perform: dynamodb:GetItem on resource: arn:aws:dynamodb:ap-south-1:137141637317:table/dam_user_filter because no identity-based policy allows the dynamodb:GetItem action",
  "errorType": "ClientError",
  "requestId": "2c5dea95-94a9-4205-806d-053574e55168",
  "stackTrace": [
    "  File \"/var/task/lambda_function.py\", line 48, in lambda_handler\n    db_users = get_dynamo_db_item(DYNAMODB_TABLE_NAME, key, dynamodb)\n",
    "  File \"/var/task/lambda_function.py\", line 156, in get_dynamo_db_item\n    response = table.get_item(Key=key)\n",
    "  File \"/var/lang/lib/python3.12/site-packages/boto3/resources/factory.py\", line 581, in do_action\n    response = action(self, *args, **kwargs)\n",
    "  File \"/var/lang/lib/python3.12/site-packages/boto3/resources/action.py\", line 88, in __call__\n    response = getattr(parent.meta.client, operation_name)(*args, **params)\n",
    "  File \"/var/lang/lib/python3.12/site-packages/botocore/client.py\", line 565, in _api_call\n    return self._make_api_call(operation_name, kwargs)\n",
    "  File \"/var/lang/lib/python3.12/site-packages/botocore/client.py\", line 1021, in _make_api_call\n    raise error_class(parsed_response, operation_name)\n"
  ]
}

Function Logs
START RequestId: 2c5dea95-94a9-4205-806d-053574e55168 Version: $LATEST
event - {'awslogs': {'data': 'eyJsb2dFdmVudHMiOiBbeyJtZXNzYWdlIjogIjEwMXxzYXRpc2ggfCAgY3JlYXRlIHwgfDAgfHwwIHwgODgwIHwgdHlwZSAtIGxvY2F0aW9uLnNwYWNlIHx8IHdyaXRlIHwgZW5kX3RpbWV8fHdoaXRlIDB8fGNoYW5uZWwifV19'}}
decrypted event - {'logEvents': [{'message': '101|satish |  create | |0 ||0 | 880 | type - location.space || write | end_time||white 0||channel'}]}
Log Stream: UnknownLogStream
LAMBDA_WARNING: Unhandled exception. The most likely cause is an issue in the function code. However, in rare cases, a Lambda runtime update can cause unexpected function behavior. For functions using managed runtimes, runtime updates can be triggered by a function change, or can be applied automatically. To determine if the runtime has been updated, check the runtime version in the INIT_START log entry. If this error correlates with a change in the runtime version, you may be able to mitigate this error by temporarily rolling back to the previous runtime version. For more information, see https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html
[ERROR] ClientError: An error occurred (AccessDeniedException) when calling the GetItem operation: User: arn:aws:sts::137141637317:assumed-role/red-dam-role-b0q1toew/red-dam is not authorized to perform: dynamodb:GetItem on resource: arn:aws:dynamodb:ap-south-1:137141637317:table/dam_user_filter because no identity-based policy allows the dynamodb:GetItem action
Traceback (most recent call last):
  File "/var/task/lambda_function.py", line 48, in lambda_handler
    db_users = get_dynamo_db_item(DYNAMODB_TABLE_NAME, key, dynamodb)
  File "/var/task/lambda_function.py", line 156, in get_dynamo_db_item
    response = table.get_item(Key=key)
  File "/var/lang/lib/python3.12/site-packages/boto3/resources/factory.py", line 581, in do_action
    response = action(self, *args, **kwargs)
  File "/var/lang/lib/python3.12/site-packages/boto3/resources/action.py", line 88, in __call__
    response = getattr(parent.meta.client, operation_name)(*args, **params)
  File "/var/lang/lib/python3.12/site-packages/botocore/client.py", line 565, in _api_call
    return self._make_api_call(operation_name, kwargs)
  File "/var/lang/lib/python3.12/site-packages/botocore/client.py", line 1021, in _make_api_call
    raise error_class(parsed_response, operation_name)END RequestId: 2c5dea95-94a9-4205-806d-053574e55168
REPORT RequestId: 2c5dea95-94a9-4205-806d-053574e55168	Duration: 2679.10 ms	Billed Duration: 2680 ms	Memory Size: 128 MB	Max Memory Used: 88 MB	Init Duration: 617.48 ms

Request ID
2c5dea95-94a9-4205-806d-053574e55168
