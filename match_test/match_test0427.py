# !/usr/bin/env python
# -*-coding:utf-8 -*-
# author:Dra Date：2018/2/24

import cv2
import numpy as np
import time
import threading


class MyThread(threading.Thread):
    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except KeyboardInterrupt:
            return None


def match(img, model, value):  # 模板和查找目标
    try:
        # 加载原始图像(RGB)
        # print(img, model, value)
        img_rgb = cv2.imread(img)
        # 创建原始图像的灰度版本，所有操作在灰度版本中处理，然后再RGB图像中使用相同坐标还原
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        # 加载将要搜索的图像模板
        tmp = cv2.imread(model, 0)
        # 记录图像模板的尺寸
        # w,h = tmp.shape[::-1]
        # 查找图像
        res = cv2.matchTemplate(img_gray, tmp, cv2.TM_CCOEFF_NORMED)
        # 设定阈值
        thread = value
        # res大于thread
        loc = np.where(res >= thread)
        px = loc[1]
        py = loc[0]
        # for pt in zip(*loc[::-1]):
        #     cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(7,249,151),2)
        # cv2.namedWindow('show',0)
        # cv2.resizeWindow('show',960,540)
        # cv2.moveWindow('show',960,540)
        # cv2.imshow("show",img_rgb)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        print(px)
        if len(px) != 0:
            # print('有')
            return px[0], py[0]
        else:
            # print('无')
            return [0, 0]
    except KeyboardInterrupt:
        print('no match')


target = '1'
b = []
image = 'autoAzure_line.png'
targets = ['chuji.png', 'guibi.png', 'qianwang.png', 'ditu8-4.png', 'boss.png', 'chuji2.png', 'queren.png']
enemy = ['diren2.png', 'diren3.png', 'diren1.png']
value = 0.75
begin_time = time.time()

ts = []
for target in targets:
    print(target)
    th = MyThread(match, args=(image, target, value))
    th.start()
    ts.append(th)
    print(ts)

for i in ts:
    i.join()
    a = th.get_result()
    print(a)
print('多线程使用时间：', time.time()-begin_time)

# for target in targets:
#     a = match(image, target, value)
#     print(a, 11)
#     if a[0] != 0:
#         break


if a[0] == 0:
    for i in range(len(enemy)):
        a = (match(image, enemy[i], 0.55))
        b.append(a)
    if a[0] == 0:
        print(2)
        a = [250, 250]
    c = sum(b[0]), sum(b[1]), sum(b[2])
    if sum(c) != 0:
        print((c.index(min(filter(None, c)))))
        a = b[c.index(min(filter(None, c)))]
        print(c)
end_time = time.time()
print(a)

print(target, end_time-begin_time)

print(a, b)


# TODO  进行多进程实验2018年4月27日20:29:13
