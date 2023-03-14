n = int(input("日期:"))

date = n % 7

if (date == 0):
    print("7")
else:
    print(date)