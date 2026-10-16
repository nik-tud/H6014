a = 66528
b = 52920

remainder = 1
while remainder != 0:
    quotient = a // b
    remainder = a % b
    a = b
    b = remainder
print(a)