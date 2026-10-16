import sys
import hashlib
import binascii
# 1. FIX: Use the official PyCryptodome padding module
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Cipher import DES

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

plaintext = val.encode('utf-8')
password_bytes = password.encode('utf-8')

def encrypt(plaintext, key, mode):
    encobj = AES.new(key, mode)
    return encobj.encrypt(plaintext)

def decrypt(ciphertext, key, mode):
    encobj = AES.new(key, mode)
    return encobj.decrypt(ciphertext)

key = hashlib.sha256(password_bytes).digest()

plaintext = pad(plaintext, block_size=AES.block_size, style='pkcs7')

hex_padded = binascii.hexlify(bytearray(plaintext)).decode('utf-8')
print("After padding (CMS): " + hex_padded)

ciphertext = encrypt(plaintext, key, AES.MODE_ECB)
hex_cipher = binascii.hexlify(bytearray(ciphertext)).decode('utf-8')
print("Cipher (ECB): " + hex_cipher)

decrypted_padded = decrypt(ciphertext, key, AES.MODE_ECB)

decrypted_bytes = unpad(decrypted_padded, block_size=AES.block_size, style='pkcs7')

print(" decrypt: " + decrypted_bytes.decode('utf-8'))

plaintext = val
