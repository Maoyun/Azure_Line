# !/usr/bin/env python
# -*-coding:utf-8 -*-
# author:Dra Date：2018/4/2


a = [21, 22, 54, 2, 38, 12, 27]

b = int(input())
d = 0
for i in range(len(a)):
    if a[i] == b:
        d +=1
        print(i)
if d == 0:
    print(-1)
