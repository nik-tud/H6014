import hashlib
import passlib.hash
import sys

salt = bytes("ZDzPE45C", 'utf-8')
strings = ['changeme', '123456', 'password']

for string in strings:
	print("PBKDF2 (SHA1): " + passlib.hash.pbkdf2_sha1.encrypt(string, salt=salt))
	print("PBKDF2 (SHA256): " + passlib.hash.pbkdf2_sha256.encrypt(string, salt=salt))

