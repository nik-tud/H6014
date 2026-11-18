# This is the program we believe was used to encode the intercepted message.
# some of the retrieved program was damaged (show as &&&&)
# Can you use this to figure out how it was encoded and decode it? 
# Good Luck

# Translation of the original code to Python3
# Any code contained in a comment is the original Python2 code that was given to us

import string
import random
from base64 import b64encode, b64decode

# secret = '&&&&&&&&&&&&&&' # We don't know the original message or length
secret = 'Why do elephants have big ears?' # uncovered message

secret_encoding = ['step1', 'step2', 'step3']

# def step1(s):
#	_step1 = string.maketrans("zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA","mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON")
#	return string.translate(s, _step1)
def step1(s):
	_step1 = str.maketrans("zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA","mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON")
	return s.translate(_step1)

# def step2(s):
#	 return b64encode(s)
def step2(s):
	# plain.encode() converts text by byte, b64encode then encodes it to base64 
	# lastly we decode it back to text from bytes so we can use it in the next steps
    return b64encode(s.encode()).decode()

# def step3(plaintext, shift=4):
#    loweralpha = string.ascii_lowercase
#    shifted_string = loweralpha[shift:] + loweralpha[:shift]
#    converted = string.maketrans(loweralpha, shifted_string)
#    return plaintext.translate(converted)
def step3(plaintext, shift=4):
    loweralpha = string.ascii_lowercase
    shifted_string = loweralpha[shift:] + loweralpha[:shift]
    converted = str.maketrans(loweralpha, shifted_string)
    return plaintext.translate(converted)

# def make_secret(plain, count):
#	 a = '2{}'.format(b64encode(plain))
#	 for count in xrange(count):
#		 r = random.choice(secret_encoding)
#		 si = secret_encoding.index(r) + 1
#		 _a = globals()[r](a)
#		 a = '{}{}'.format(si, _a)
#	 return a

def make_secret(plain, count):
	a = '2{}'.format(b64encode(plain.encode()).decode())
	for count in range(count):
		r = random.choice(secret_encoding)
		si = secret_encoding.index(r) + 1
		_a = globals()[r](a)
		a = '{}{}'.format(si, _a)
	return a

# if __name__ == '__main__':
# 	 print((make_secret(secret, count=&&&)))
# Using a random count of 123
if __name__ == '__main__':
	print((make_secret(secret, count=123)))
