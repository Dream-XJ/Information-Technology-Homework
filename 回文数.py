x = int(input("x:"))
t = x
s = 0

while (t != 0):
    s = s * 10 + t % 10
    t = t // 10

if (x == s):
    print("yes")
else:
    print("no")