#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      n1280462
#
# Created:     21/10/2020
# Copyright:   (c) n1280462 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

suit = ["S","C","D","H"]
num = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
c = [list(map(int,input().split()))for i in range(5)]
for i in range(5):
    s = c[i][0]
    n = c[i][1]-1
    print (suit[s] + num[n] , end = " ")
print()

pc = 0
mc = 0
mn = 0
ff = True
sf = True

for i in range(1,5):
    for j in range(4):
        if c[j][1] > c[i][1]:
            x = c[i][1]
            c[i][1] = c[j][1]
            c[j][1] = x

for i in range(4):
    if c[i][1] == c[i+1][1]:
        mc += 1
        if i == 3:
            if mc == 1:
                pc += 1
            elif mc > 1:
                mn = mc
    else:
        if mc == 1:
            pc += 1
        elif mc > 1:
            mn = mc
        mc = 0

    if ff == True and c[i][0] != c[i+1][0]:
        ff = False

    if sf == True and c[i][1] != c[i+1][1]-1:
        if (c[i][1] != 1 or c[i+1][1] != 10)\
        and (c[i][1] != 2 or c[i+1][1] != 11)\
        and (c[i][1] != 3 or c[i+1][1] != 12)\
        and (c[i][1] != 4 or c[i+1][1] != 13):
            sf = False

if sf == True and ff == True:
    if c[0][1] == 1 and c[1][1] == 10:
        yaku = "ロイヤルストレートフラッシュ"
    else:
        yaku = "ストレートフラッシュ"
elif mn > 1:
    if mn == 3:
        yaku = "フォーカード"
    else:
        if pc > 0:
            yaku = "フルハウス"
        else:
            yaku = "スリーカード"
elif ff == True:
    yaku = "フラッシュ"
elif sf == True:
    yaku = "ストレート"
elif pc > 0:
    if pc > 1:
        yaku = "ツーペア"
    else:
        yaku = "ワンペア"
else:
    yaku = "ハイカード"

print (yaku)