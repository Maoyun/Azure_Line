# !/usr/bin/env python
# -*-coding:utf-8 -*-
# author:Dra Date：2018/3/29


a = [0, 1, 2, 3, 5, 4, 6, 7, 8, 9]
b = []

for i in range(len(a)):
    if a[i]% 2 == 0:
        b.append(a[i])
print(b)

b = sum(b)

print(b)
