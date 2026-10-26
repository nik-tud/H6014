import os,json
from pwn import remote


def reverse_scramble_block(block):
    for _ in range(40):
        block = rotate_left(block, 17)
        block = xor(X_bytes, block)
        block = rotate_right(block, 6)
        block = xor(W_bytes, block)
    return block

def solve():
    r = remote("socket.cryptohack.org", 13405)
    r.recvline()

    initial_state = xor(Y_bytes, Z_bytes)
    b = os.urandom(32)
    scr = scramble_block(b)

    i=1
    mix_in2 = os.urandom(32)
    mix_in1 = xor(scr, mix_in2)

    mix_in2 = rotate_right(mix_in2, i+6)
    mix_in2 = xor(mix_in2, X_bytes)
    mix_in2 = rotate_left(mix_in2, i+11)

    b2 = reverse_scramble_block(mix_in1)
    b3 = reverse_scramble_block(mix_in2)

    assert cryptohash(b2+b3) == cryptohash(b)
    r.sendline(json.dumps({"m1":(b2+b3).hex(), "m2":b.hex()}).encode())
    print(r.recvall().decode())
    return json.dumps({"m1":(b2+b3).hex(), "m2":b.hex()})

print(solve())