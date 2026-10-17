g = 2879
N = 9929
x = 6
y = 9

A = pow(g, x, N)
print(A)
B = pow(g, y, N)
print(B)

Bob = pow(B, x, N)
Alice = pow(A, y, N)
print(Bob)
print(Alice)
print(Bob == Alice)