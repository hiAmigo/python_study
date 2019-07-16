import base64

print(base64.b64encode(b'binarystring'))
print(base64.b64decode(b'YmluYXJ5c3RyaW5n'))

print(base64.urlsafe_b64encode(b'\sfs\sfs\23\adgds\sfdgsdf'))
print(base64.urlsafe_b64decode(b'XHNmc1xzZnMTB2RnZHNcc2ZkZ3NkZg=='))