# Many Time Pad Decryption
# all code converted to Python from Java solution by https://github.com/madison-freeman/stream-cipher

import sys

def main(input_file):
    with open(input_file, 'r') as f:
        messages = f.read()
    
    # Convert hex messages to byte arrays for later XORing
    byte_messages = convert_hex_to_bytes(messages)

    plaintext_messages = decrypt_messages(byte_messages)

    for plaintext in plaintext_messages:
        print("".join(plaintext))

def convert_hex_to_bytes(hex_string):
    # Split the hex strings into individual encrypted messages
    messages = hex_string.split("\n\n")

    byte_messages = []
    for message in messages:
        message = "".join(message.split())
        # https://www.geeksforgeeks.org/python/convert-hex-string-to-bytes-in-python/
        byte_array = bytearray.fromhex(message)
        byte_messages.append(byte_array)
    return byte_messages

def decrypt_messages(byte_messages):
    # Create an array of '_' characters the length of our cipher texts so that we can fill in 
    # letters we know about and the rest will be blanks 
    # (the letters we couldn't recover due to no space being in that position in all other plain texts)
    plaintext = [
        ['_' for _ in ct]
        for ct in byte_messages
    ]

    # Take two cipher texts for testing
    for i in range(len(byte_messages)):
        for j in range(len(byte_messages)):
            # We don't want to XOR a cipher text with itself
            if i == j:
                continue
            # Take the smaller cipher text message as we can only encrypt the whole smallest message,
            # because otherwise we will just be XORing with blank space
            min_length = min(len(byte_messages[i]), len(byte_messages[j]))
            for k in range(min_length):
                x = byte_messages[i][k] ^ byte_messages[j][k]
                if is_letter(x):
                    if check_all(i, byte_messages[i][k], k, byte_messages):
                        for l in range(len(plaintext)):
                            if k >= len(plaintext[l]) or plaintext[l][k] != '_':
                                continue
                            # We get the letter XORed with a space i.e. 'a' XOR ' ' = 'A' and 
                            # convert it back to its original case by XORing with a space again
                            x = (byte_messages[i][k] ^ byte_messages[l][k] ^ ord(' '))
                            # If it returned 0 we know that it was two spaces as ' ' XOR ' ' = 0
                            if l == i or x == 0:
                                plaintext[l][k] = ' '
                            else:
                                plaintext[l][k] = chr(x)
    return plaintext
                            
                
# Check what the XOR output is with our current character 
# and all other cipher texts at that position
def check_all(array_index, character, character_index, cipher_texts):
    error_count = 0
    for j in range(len(cipher_texts)):
        if j == array_index or len(cipher_texts[j]) <= character_index:
            continue
        x = character ^ cipher_texts[j][character_index]

        # if we get 0 that means we XORed two spaces together
        if x == 0:
            continue

        if not is_letter(x):
            error_count += 1
            # If we don't get a real letter back 3 or more times it likely wasn't a space
            if error_count > 2:
                return False
    return True

# If this returns true, it is possible we have a space in that position
def is_letter(byte):
    return (
        ord('A') <= byte <= ord('Z') or ord('a') <= byte <= ord('z')
    )

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ManyTimePad.py input_file with hex messages encoded with a single stream cipher key")
        sys.exit(1)
    main(sys.argv[1])