n = int(input("n:"))
k = int(input("n:"))
a = 0
b = 0

for i in range(0, n + 1, 1):
    if (i % k == 0):
        a = a + 1
    else:
        b = b + 1
