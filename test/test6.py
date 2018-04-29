# !/usr/bin/env python
# -*-coding:utf-8 -*-
# author:Dra Date：2018/4/27

#coding=utf-8
#
# '''
# 多线程
#
#
# 进程 pid 唯一标示符
# 使用kill 杀死进程
#
#
# 主线程 创造一个进程的时候，会创造一个线程，这个线程被称为主线程
# 一个进程里只有一个主线程
#
#
# python里的多线程，不是真正意义上的多线程。
#
# 全局锁
#
# 在任意的指定时间里，有且只有一个线程在运行
#
# a b c
# '''

import threading
import time


def test(p):
    time.sleep(0.001)
    print (p)


ts = []

for i in range(0,15):
    th = threading.Thread(target=test,args=[i])
    th.start()
    ts.append(th)


for i in ts:
    i.join()

print("hoho,end!!!!!")