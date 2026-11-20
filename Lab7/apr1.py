import passlib.hash

salt = "PkWj6gM4"
strings = ['changeme', '123456', 'password']
for string in strings:
	print("APR1: " + passlib.hash.apr_md5_crypt.encrypt(string))
