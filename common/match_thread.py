# !/usr/bin/env python
# -*-coding:utf-8 -*-
# author:Dra Date：2018/2/22

import os
import sys
import random
import cv2
import time
import numpy as np
import threading


class MyThread(threading.Thread):
    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args
        self.result = None

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except KeyboardInterrupt:
            return None


def match(img, model, value):  # 模板和查找目标
    try:
        if model in ["diren1.png", 'diren2.png', 'diren3.png']:
            value = 0.65
        elif model == 'boss.png':
            value = 0.58
        print('value:', value)
        # 确定模型类型与ID
        # 也可以使用in来做判断
        targets = ['chuji.png', 'guibi.png', 'qianwang.png', 'ditu8-4.png', 'boss.png', 'chuji2.png', 'queren.png',
                   'diren2.png', 'diren3.png', 'diren1.png']
        modelid = targets.index(model)
        # 加载原始图像(RGB)
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
        if len(px) != 0:
            print(px[0], py[0], model)
            return px[0], py[0], modelid

        else:
            # print([0, 0, 0])
            return [0, 0]

    except KeyboardInterrupt:
        print('no match')


def pull_screenshot():  # 获取截图
    os.system('adb shell screencap -p /sdcard/autoAzure_line.png')  # png效果最好
    os.system('adb pull /sdcard/autoAzure_line.png .')


def touch(touch_x1, touch_y1):  # adb点击目标，添加了随机数避免被ban
    cmd = 'adb shell input tap {x1} {y1}'.format(
        x1=touch_x1 + random.randint(10, 100),
        y1=touch_y1 + random.randint(20, 50),
        # x2=touch_x1 + random.randint(0,10),
        # y2=touch_y1 + random.randint(0,10),
        # duration=random.randint(10,300),
    )
    os.system(cmd)
    return touch_x1, touch_y1


def touch_boss(touch_x1, touch_y1):
    cmd = 'adb shell input tap {x1} {y1}'.format(
        x1=touch_x1 + random.randint(30, 80),
        y1=touch_y1 + random.randint(30, 80),
        # x2=touch_x1 + random.randint(0,10),
        # y2=touch_y1 + random.randint(0,10),
        # duration=random.randint(10,300),
    )
    os.system(cmd)
    return touch_x1, touch_y1


def touch_diren(touch_x1, touch_y1):
    cmd = 'adb shell input tap {x1} {y1}'.format(
        x1=touch_x1 + random.randint(-10, 50),
        y1=touch_y1 + random.randint(-10, 50),
        # x2=touch_x1 + random.randint(0,10),
        # y2=touch_y1 + random.randint(0,10),
        # duration=random.randint(10,300),
    )
    os.system(cmd)
    return touch_x1, touch_y1


def swipe_screen(x1, y1, x2, y2):
    cmd = 'adb shell input swipe {x1} {y1} {x2} {y2}'.format(
        x1=x1 + random.randint(-10, 20),
        y1=y1 + random.randint(-10, 20),
        x2=x2 + random.randint(0, 20),
        y2=y2 + random.randint(0, 20),
        # duration=random.randint(10,300),
    )
    os.system(cmd)
    return x1, y1


def main():
    count = 0
    while True:
        # b = []
        modelid = 0
        flag = 0
        result_a = [0, 0]
        begin_time1 = time.time()
        pull_screenshot()
        print("截图时间", time.time()-begin_time1)
        image = "autoAzure_line.png"
        targets = ['chuji.png', 'guibi.png', 'qianwang.png', 'ditu8-4.png', 'boss.png', 'chuji2.png', 'queren.png',
                   'diren2.png', 'diren3.png', 'diren1.png']
        # enemy = ['diren2.png', 'diren3.png', 'diren1.png']
        value = 0.75
        begin_time = time.time()
        ts = []
        for target in targets:
            # print(target)
            th = MyThread(match, args=(image, target, value))
            th.start()
            ts.append(th)
            # print(ts)

        print('多线程使用时间1：', time.time() - begin_time)
        for th in ts:  # 获取线程处理结果
            th.join()
            a = th.get_result()
            # print(a, target)
            if a[0] != 0 and flag ==0:
                if a[2] in range(7):
                    result_a[0:2] = a[0:2]
                    modelid = a[2]
                    print(result_a, modelid)
                    flag = 1
                else:
                    if result_a[1] >= a[1]:  # 预留的处理找到敌人后先打哪个的位置 目前是先打最下面的
                        result_a[0:2] = result_a[0:2]  # 取前两位作为坐标
                        modelid = a[2]
                        # result_a = a
                        # print('####################')
                    else:
                        result_a[0:2] = a[0:2]
                        modelid = a[2]
                        # print("@@@@@@@@@@@@@@@@@@@@")
        print('多线程使用时间2：', time.time() - begin_time)
        match_time = time.time() - begin_time
        print("匹配时间", match_time)
        # if result_a[0] == 0:
        #     for i in range(len(enemy)):
        #         result_a = (match(image, enemy[i], 0.6))
        #         b.append(result_a)
        #     c = sum(b[0]), sum(b[1]), sum(b[2])
        #     if sum(c) != 0:
        #         result_a = b[c.index(min(filter(None, c)))]
        #         print(filter(None, c))
        #     else:
        #         print(2)
        #         result_a = [250, 250]
        if result_a[0] == 0:
            result_a = [380, 0]
        x = result_a[0]
        y = result_a[1]
        # touch(xbn  ,y)
        # print('识别模型：', target)
        print('识别结果：', result_a)
        # print(b)
        if modelid == 4:
            print(touch_boss(x, y), 'boss'+targets[modelid])
            count += 1
            time.sleep(2)
        elif modelid in [7, 8, 9]:
            print(touch_diren(x, y), 'diren'+targets[modelid])
        elif modelid == 2:
            print(touch(x, y))
            # flag = 1
        # elif flag == 1 and target == 'qianwang.png':
        #     print(touch(x, y))
        #     time.sleep(0.8)
        #     print(swipe_screen(100, 100, 100, 450))
        #     flag = 0
        else:
            print(touch(x, y), '其他'+targets[modelid])
        wait = random.random() + 0  # 停0~9秒 指数越高平均间隔越短
        print("等待时间", wait)
        time.sleep(wait)
        print('boss:', count)
        print('运行时间：', time.time()-begin_time1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        os.system('adb kill -server') 
        print('bye')
        exit(0)

# TODO: 过程中要添加随机点击-OK
# TODO：寻找LV小怪的时候随机指数要反向写-CANCEL
# TODO：改善找到boss后要经过多次点击进入boss,战斗过程中程序失败-to do
# TODO: 改为三通道匹配-CANCEL
# TODO: 决策时间太慢了，boss与小怪的匹配程度太低  了-OK
# TODO: 增加滑动屏幕更改地图位置功能-OK
# TODO: 增加统计战利品功能
# TODO: 改善现有的boss数量统计功能
# TODO: 根据实际情况滑动地图，因为地图并不是在右下角总有敌人
# 0329
# TODO: 根据新出活动更改寻找敌人的方式——同时找三种敌人，并且先打左上角的-OK
# TODO: 打不到就选下一个
# 0427
# TODO: 要求所有搜索做到并发多线程
# 0429
# 解决了关于碰到多个模型同时出现，但是要求优先度的问题
# TODO: 需要解决match到相同模型时需要选择适合目标的情况，还需要屏幕向下滑动一下(8-4)
