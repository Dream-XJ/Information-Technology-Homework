x = float(input("x:"))
y = float(input("y:"))

bmi = x / (y ** 2)

if (bmi < 18):
    print("轻")
else:
    if (bmi > 26):
        print("重")
    else:
        print("正常")
