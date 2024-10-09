import gzip
import base64

# Sample log data
log_data = "104|jaibir | |create |0|0|0|9223372036854775807|1073774976|983539|Wed, 9 Oct 2024 12:16:28:157"

# Compress the log data
compressed_data = gzip.compress(log_data.encode('utf-8'))

# Base64 encode the compressed data
base64_encoded_data = base64.b64encode(compressed_data).decode('utf-8')

print(base64_encoded_data)
