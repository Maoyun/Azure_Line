# !/usr/bin/env python
# -*-coding:utf-8 -*-
# author:Dra Date：2018/4/2


a = [21, 22, 54, 2, 38, 12, 27]
temp = [0, 1, 2, 3, 4, 5, 6]
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j] <= a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            temp[j], temp[j+1] = temp[j+1], temp[j]

print(a, temp)
print(a[0], temp[0])
