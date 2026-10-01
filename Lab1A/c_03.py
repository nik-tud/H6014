message = int(input('Enter message: '))
e = int(input('Enter exponent: '))
p = int(input('Enter prime '))
cipher = (message ** e) % p
print(cipher)