n = 316
cnt = 1

while (cnt != n):
    cntr = n-cnt
    if (cnt % 11 == 0) and (cntr % 13 == 0):
        print(cnt, cntr)
    cnt += 1
