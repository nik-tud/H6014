from Crypto.Cipher import AES
from pwn import xor

KEY = "1e703a2b852f9dabc566472bd45941ce56340e6c2e076f1f9fc09bf325a9dd63"
FLAG = "63727970746f7b626c30636b5f633170683372355f3472335f663435375f217d"
ciphertext = "7d02435bf140e6c9a95624408b3a70be3e077c5971331d2cc0a6afc612f6fc1e"

@chal.route('/block_cipher_starter/decrypt/<ciphertext>/')
def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


@chal.route('/block_cipher_starter/encrypt_flag/')
def encrypt_flag():
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(FLAG.encode())

    return {"ciphertext": encrypted.hex()}