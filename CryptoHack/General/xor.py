from pwn import xor

import cv2
import numpy as np

# Starter
print(xor("label", 13))

# Properties
key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key1_2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_key123 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

# (A ^ B) ^ A = B ^ 0 = B 
# (key1 ^ key2) ^ key1 = key2 ^ 0 = key2
key2 = xor(bytes.fromhex(key1_2), key1)

# (A ^ B) ^ A = B ^ 0 = B 
# (key2 ^ key3) ^ key2 = key3 ^ 0 = key3
key3 = xor(bytes.fromhex(key2_3), key2)

flag = xor(bytes.fromhex(flag_key123), key1, key2, key3)

print(flag)

# Favourite byte
key = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
for x in range(256):
    try:
        decoded = bytes([b ^ x for b in key])
        text = decoded.decode('utf-8')
        if "crypto" in text:
            print(f"[+] Key: {x}")
            print(f"[+] Flag: {text}")
            break
    except UnicodeDecodeError:
        continue

# You either know, XOR you don't
hexString = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
flag = bytes.fromhex("crypto{".encode().hex())

key = xor(flag, hexString)[0:7] + bytes('y'.encode('utf-8'))
print(xor(key, hexString))

# Lemur XOR
image1 = cv2.imread('flag_7ae18c704272532658c10b5faad06d74.png')
image2 = cv2.imread('lemur_ed66878c338e662d3473f0d98eedbd0d.png')
dest_xor = cv2.bitwise_xor(image1, image2, mask=None)
cv2.imshow('Bitwise XOR', dest_xor)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
