import passlib.hash

salt = "8sFt66rZ"

strings = ['changeme', '123456', 'password']

for string in strings:
	print("SHA1: " + passlib.hash.sha1_crypt.encrypt(string, salt=salt))
	print("SHA256: " + passlib.hash.sha256_crypt.encrypt(string, salt=salt))
	print("SHA512: " + passlib.hash.sha256_crypt.encrypt(string, salt=salt))
