# !/usr/bin/env python
# -*-coding:utf-8 -*-
# author:Dra Date：2018/4/3


a = 123456
b = []              # 数组，用来接最后获得的数
n = 0               # 计数器，用来计算要除的  次方
temp = a            # a的一个备份，避免直接处理a
while temp > 1:     # 一个循环，用来计算a有几位数
    temp /= 10      # temp = temp/10
    n += 1          # n加一，用于计数
for i in range(n, 0, -1):   # 主要部分，range(n, 0, -1)是说一个从8，7，6，5，4，3，2，1的循环，与原来从0-7是相反的且多个8少个0
    if i == n:              # 若是第一个数，单独做处理
        c = a // 10**(i-1)  # 数a除以10的i-1次方，取商的整数
    else:
        c = a % 10**i // 10**(i-1)  # 从第二个数开始，每个数先与10的i次方求余数，然后把余数除以10的i-1次方，取整
    b.append(c)                     # 每个c加到数组b的最后
    print(c)
print(b)
# print(x)
