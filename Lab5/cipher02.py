import sys
import hashlib
import binascii
# 1. FIX: Use the official PyCryptodome padding module
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Cipher import DES
import base64

if len(sys.argv) > 1:
    val = sys.argv[1]
else:
    print("Usage: python3 cipher01.py <plaintext> <password>")
    sys.exit(1)

if len(sys.argv) > 2:
    password = sys.argv[2]
else:
    print("Usage: python3 cipher01.py <plaintext> <password>")
    sys.exit(1)


cipher = base64.b64decode(val).hex()
password_bytes = password.encode('utf-8')

def encrypt(plaintext, key, mode):
    encobj = AES.new(key, mode)
    return encobj.encrypt(plaintext)

def decrypt(ciphertext, key, mode):
    encobj = AES.new(key, mode)
    return encobj.decrypt(ciphertext)

key = hashlib.sha256(password_bytes).digest()

ciphertext = binascii.unhexlify(cipher)

plaintext = decrypt(ciphertext, key, AES.MODE_ECB)
print(plaintext)

try: 
    plaintext = unpad(plaintext, block_size=AES.block_size, style='pkcs7')
    print(" decrypt: " + plaintext.decode('utf-8'))
except:
    print("Error!")

plaintext = val
