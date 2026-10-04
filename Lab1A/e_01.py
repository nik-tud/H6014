a = int(input("Enter the value for a: "))
seed = int(input("Enter the seed value: "))
c = int(input("Enter the value for c: "))
m = int(input("Enter the value for m: "))

i = 0
while i < 10:
    seed = (a * seed + c) % m
    print(seed)
    i += 1