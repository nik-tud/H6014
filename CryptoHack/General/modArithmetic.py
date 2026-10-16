# Modular Arithmetic 1
print(min(11 % 6, 8146798528947 % 17))

# Modular Arithmetic 2
print((3 ** 17) % 17)
print((5 ** 17) % 17)
print((7 ** 16) % 17)
# Fermat's Little Theorem => a**(p-1) mod p = 1

# Modular Inverting
# Fermat's Little Theorem => a**(-1) is equal to **(m-2) mod m
print((3**11) % 13)