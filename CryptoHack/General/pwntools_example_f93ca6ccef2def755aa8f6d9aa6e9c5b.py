from pwn import * # pip install pwntools
import json
import codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


for i in range(100):
    received = json_recv()

    print("Received type: ")
    rec_type = received["type"]
    print(rec_type)
    print("Received encoded value: ")
    rec_enc = received["encoded"]
    print(rec_enc)

    if (rec_type == "base64"):
        to_send = {
            "decoded": base64.b64decode(rec_enc).decode() 
        }
        json_send(to_send)
        
    elif (rec_type == "rot13"):
        to_send = {
            "decoded": codecs.decode(rec_enc, 'rot_13') 
        }
        json_send(to_send)
        
    elif (rec_type == "bigint"):
        to_send = {
            "decoded": bytes.fromhex(rec_enc.replace("0x","")).decode()
        }
        json_send(to_send)
        
    elif (rec_type == "utf-8"):
        to_send = {
            "decoded": "".join([chr(b) for b in rec_enc])
        }
        json_send(to_send)
        
    elif (rec_type == "hex"):
        to_send = {
            "decoded": bytes.fromhex(rec_enc.replace("0x","")).decode('utf-8')
        }
        json_send(to_send)

    

json_recv()