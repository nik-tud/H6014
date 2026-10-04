# Sieve of Eratosthenes Method for checking if a number is prime
# https://www.geeksforgeeks.org/python/python-program-to-check-whether-a-number-is-prime-or-not/
def isprime(n):
    if n < 2:
        return False

    s = [True] * (n + 1)
    s[0] = s[1] = False

    for i in range(2, int(n**0.5) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    return s[n]

val1 = int(input("Enter the first number (base): "))
val2 = int(input("Enter the second number (exponent): "))

val3 = int(input("Enter the third number (modulus): "))
while not(isprime(val3)):
    print("Modulus should be prime")
    val3 = int(input("Enter the third number (modulus): "))

print((val1 ** val2) % val3)