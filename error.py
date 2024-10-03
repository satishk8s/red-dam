error 

Test Event Name
damtest

Response
{
  "errorMessage": "Not a gzipped file (b'{\"')",
  "errorType": "BadGzipFile",
  "requestId": "821b8252-e384-4d40-ba5f-997df2187040",
  "stackTrace": [
    "  File \"/var/task/lambda_function.py\", line 19, in lambda_handler\n    cw_logs = gzip.GzipFile(fileobj=BytesIO(base64.b64decode(cw_data, validate=True))).read()\n",
    "  File \"/var/lang/lib/python3.12/gzip.py\", line 324, in read\n    return self._buffer.read(size)\n",
    "  File \"/var/lang/lib/python3.12/_compression.py\", line 118, in readall\n    while data := self.read(sys.maxsize):\n",
    "  File \"/var/lang/lib/python3.12/gzip.py\", line 527, in read\n    if not self._read_gzip_header():\n",
    "  File \"/var/lang/lib/python3.12/gzip.py\", line 496, in _read_gzip_header\n    last_mtime = _read_gzip_header(self._fp)\n",
    "  File \"/var/lang/lib/python3.12/gzip.py\", line 456, in _read_gzip_header\n    raise BadGzipFile('Not a gzipped file (%r)' % magic)\n"
  ]
}

Function Logs
START RequestId: 821b8252-e384-4d40-ba5f-997df2187040 Version: $LATEST
event - {'awslogs': {'data': 'eyJsb2dFdmVudHMiOiBbeyJtZXNzYWdlIjogIjEwMXxzYXRpc2ggfCAgY3JlYXRlIHwgfDAgfHwwIHwgODgwIHwgdHlwZSAtIGxvY2F0aW9uLnNwYWNlIHx8IHdyaXRlIHwgZW5kX3RpbWV8fHdoaXRlIDB8fGNoYW5uZWwifV19'}}
LAMBDA_WARNING: Unhandled exception. The most likely cause is an issue in the function code. However, in rare cases, a Lambda runtime update can cause unexpected function behavior. For functions using managed runtimes, runtime updates can be triggered by a function change, or can be applied automatically. To determine if the runtime has been updated, check the runtime version in the INIT_START log entry. If this error correlates with a change in the runtime version, you may be able to mitigate this error by temporarily rolling back to the previous runtime version. For more information, see https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html
[ERROR] BadGzipFile: Not a gzipped file (b'{"')
Traceback (most recent call last):
  File "/var/task/lambda_function.py", line 19, in lambda_handler
    cw_logs = gzip.GzipFile(fileobj=BytesIO(base64.b64decode(cw_data, validate=True))).read()
  File "/var/lang/lib/python3.12/gzip.py", line 324, in read
    return self._buffer.read(size)
  File "/var/lang/lib/python3.12/_compression.py", line 118, in readall
    while data := self.read(sys.maxsize):
  File "/var/lang/lib/python3.12/gzip.py", line 527, in read
    if not self._read_gzip_header():
  File "/var/lang/lib/python3.12/gzip.py", line 496, in _read_gzip_header
    last_mtime = _read_gzip_header(self._fp)
  File "/var/lang/lib/python3.12/gzip.py", line 456, in _read_gzip_header
    raise BadGzipFile('Not a gzipped file (%r)' % magic)END RequestId: 821b8252-e384-4d40-ba5f-997df2187040
REPORT RequestId: 821b8252-e384-4d40-ba5f-997df2187040	Duration: 19.61 ms	Billed Duration: 20 ms	Memory Size: 128 MB	Max Memory Used: 81 MB

Request ID
821b8252-e384-4d40-ba5f-997df2187040
