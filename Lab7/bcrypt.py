import hashlib
import passlib.hash

salt = 'ZDzPE45C'
string = 'hello'
string = string.encode('utf-8')

print("MD5:"+hashlib.md5(string).hexdigest())
print("SHA1:"+hashlib.sha1(string).hexdigest())
print("SHA256:"+hashlib.sha256(string).hexdigest())
print("SHA512:"+hashlib.sha512(string).hexdigest())

print("DES:"+passlib.hash.des_crypt.encrypt(string, salt=salt[:2]))
print("MD5:"+passlib.hash.md5_crypt.encrypt(string, salt=salt))
print("Sun MD5:"+passlib.hash.sun_md5_crypt.encrypt(string, salt=salt))
print("SHA1:"+passlib.hash.sha1_crypt.encrypt(string, salt=salt))
print("SHA256:"+passlib.hash.sha256_crypt.encrypt(string, salt=salt))
print("SHA512:"+passlib.hash.sha512_crypt.encrypt(string, salt=salt))

