Test Event Name
damtest

Response
{
  "statusCode": 400,
  "body": "\"Error: 'logStream' not found in log events.\""
}

Function Logs
START RequestId: 3de59afc-7f17-47cc-855d-cd095cc02f2b Version: $LATEST
event - {'awslogs': {'data': 'eyJsb2dFdmVudHMiOiBbeyJtZXNzYWdlIjogIjEwMXxzYXRpc2ggfCAgY3JlYXRlIHwgfDAgfHwwIHwgODgwIHwgdHlwZSAtIGxvY2F0aW9uLnNwYWNlIHx8IHdyaXRlIHwgZW5kX3RpbWV8fHdoaXRlIDB8fGNoYW5uZWwifV19'}}
decrypted event - {'logEvents': [{'message': '101|satish |  create | |0 ||0 | 880 | type - location.space || write | end_time||white 0||channel'}]}
Key 'logStream' not found in log events. Exiting function.
END RequestId: 3de59afc-7f17-47cc-855d-cd095cc02f2b
REPORT RequestId: 3de59afc-7f17-47cc-855d-cd095cc02f2b	Duration: 2071.26 ms	Billed Duration: 2072 ms	Memory Size: 128 MB	Max Memory Used: 87 MB	Init Duration: 558.15 ms

Request ID
3de59afc-7f17-47cc-855d-cd095cc02f2b
