# !/usr/bin/env python
# -*-coding:utf-8 -*-
# author:Dra Date：2018/3/28

import random


# 甲：
x = 1
a = 5 * x

# 乙和丙：
# b = random.randint(1, 10) * random.randint(1,10)
# c = random.randint(1, 10) * random.randint(1,10)
b = 100
c = 5

y = [a, b, c]
temp = ['a', 'b', 'c']
deng = []

for i in range(len(y)-1):
    for j in range(len(y)-i-1):
        if y[j] > y[j+1]:
            y[j], y[j+1] = y[j+1], y[j]
            temp[j], temp[j+1] = temp[j+1], temp[j]
        if y[j] == y[j+1]:
           print(temp[j] + "等于" + temp[j+1])

print(y)
print(temp)

for i in range(len(y)):
    if y[i] >= 80:
        print(temp[i] + '为大矩形')
    elif y[i] >= 60:
        print(temp[i] + '为中矩形')
    else:
        print(temp[i] + '为小矩形')


