import base64

str = "crypto1"
print(base64.b64encode(str.encode('utf-8')))

str = "1"
print(base64.b64encode(str.encode('utf-8')))
