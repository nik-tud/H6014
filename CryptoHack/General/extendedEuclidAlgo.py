p = 26513
q = 32321

x0, x1, y0, y1 = 1, 0, 0, 1
while q:
    r = p // q
    p, q = q, p % q
    x0, x1 = x1, x0 - r * x1
    y0, y1 = y1, y0 - r * y1

print("GCD is", p)
print("x =", x0, ", y =", y0)