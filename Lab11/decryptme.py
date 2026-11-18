# Program used to decrypt the intercepted encrypted message
# Each step is the reverse of the encoding steps in encryptme.py starting with step1

import string
from base64 import b64decode

import sys

# Used for ROT13 encryption
# https://stackoverflow.com/questions/3269686/short-rot13-function-python
import codecs

# ROT13 is self inverse so we can just repeat the encoding step to undo it
def undo_step1(s):
    return codecs.encode(s, 'rot_13')

# If we wanted to do the above without using the codecs library:
# def undo_step1(s):
#     _step1 = str.maketrans("zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA","mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON")
#     return s.translate(_step1)

def undo_step2(s):
    return b64decode(s).decode("utf-8")

def undo_step3(s, shift=4):
    loweralpha = string.ascii_lowercase
    # step3 shifted lowercase forward by 4, so shift back by 4
    unshifted = str.maketrans(loweralpha, loweralpha[-shift:] + loweralpha[:-shift])
    return s.translate(unshifted)

# each step adds the step number to the front of the string, so we can use that
# to determine which step to undo next
undo_steps = {"1": undo_step1, "2": undo_step2, "3": undo_step3}
def decode(message):
    s = message.strip()

    while s and s[0] in undo_steps:
        # print("ENCODED TEXT FOR STEP", s[0] + ":", s[1:])
        marker, body = s[0], s[1:]
        s = undo_steps[marker](body)
    return s


if __name__ == "__main__":
    # Read the given file as input (intercepted.txt in this case)
    file = sys.argv[1] if len(sys.argv) > 1 else None
    with open(file) as f:
        encoded = f.read()
    
    print(decode(encoded))