# Sample for reference
# Encode/Decode base 64

import base64

# The message to encode
eMessage = ""
# The message to decode
dMessage = ""

# Encode Function
def encode64(message=eMessage):
	message_bytes = message.encode("ascii")
	base64_bytes = base64.b64encode(message_bytes)
	return base64_bytes.decode("ascii")

# Decode Function
def decode64(message=dMessage):
	base64_bytes = message.encode("ascii")
	message_bytes = base64.b64decode(base64_bytes)
	return message_bytes.decode("ascii")

# Test Statements
#print(encode64("Hello world"))
#print(decode64("SGVsbG8gd29ybGQ="))