import math

a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))

delta = b ** 2 - 4 * a * c
if (delta > 0):
    print((-b + math.sqrt(delta)) / 2 * a, (-b - math.sqrt(delta)) / 2 * a)
else:
    if (delta == 0):
        print(-b + math.sqrt(delta) / 2 * a)
    else:
        print("无解")

