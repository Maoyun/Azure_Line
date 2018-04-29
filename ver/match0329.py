# !/usr/bin/env python
# -*-coding:utf-8 -*-
# author:Dra Date：2018/2/22

import os
import sys
import random
import cv2
import time
import numpy as np


def match(img, model, value):  # 模板和查找目标
    try:
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
            return px[0], py[0]
        else:
            return []
    except KeyboardInterrupt:
        print('no match')


def pull_screenshot():  # 获取截图
    os.system('adb shell screencap -p /sdcard/autoAzure_line.png')
    os.system('adb pull /sdcard/autoAzure_line.png .')


def touch(touch_x1, touch_y1):  # adb点击目标，添加了随机数避免被ban
    cmd = 'adb shell input tap {x1} {y1}'.format(
        x1=touch_x1 + random.randint(50, 150),
        y1=touch_y1 + random.randint(20, 80),
        # x2=touch_x1 + random.randint(0,10),
        # y2=touch_y1 + random.randint(0,10),
        # duration=random.randint(10,300),
    )
    os.system(cmd)
    return touch_x1, touch_y1


def touch_boss(touch_x1, touch_y1):
    cmd = 'adb shell input tap {x1} {y1}'.format(
        x1=touch_x1 + random.randint(100, 230),
        y1=touch_y1 + random.randint(100, 150),
        # x2=touch_x1 + random.randint(0,10),
        # y2=touch_y1 + random.randint(0,10),
        # duration=random.randint(10,300),
    )
    os.system(cmd)
    return touch_x1, touch_y1


def touch_diren(touch_x1, touch_y1):
    cmd = 'adb shell input tap {x1} {y1}'.format(
        x1=touch_x1 + random.randint(-50, 50),
        y1=touch_y1 + random.randint(-80, 20),
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
    flag = 0
    while True:
        pull_screenshot()
        a = []
        image = "autoAzure_line.png"
        targets = ['chuji.png', 'guibi.png', 'qianwang.png', 'ditu3-4.png', 'boss.png', 'diren1.png', 'queren.png']
        enemy = ['diren2.png', 'diren3.png', 'chuji2.png', ]
        value = 0.75
        for target in targets:
            a = match(image, target, value)
            if len(a) == 0:
                for index in enemy:
                    a.append(match(image, index, 0.7))
                print(a)
                if a != 0:
                    break
                else:
                    a = [250, 250]
            else:
                break
        x = a[0]
        y = a[1]
        # touch(xbn  ,y)
        print(target)
        print(a)
        if target == 'boss.png':
            print(touch_boss(x, y))
            count += 1
            time.sleep(2)
        elif target == 'diren.png':
            print(touch_diren(x, y))
        elif flag == 0 and target == 'qianwang.png':
            print(touch(x, y))
        #     flag = 1
        # elif flag == 1 and target == 'qianwang.png':
        #     print(touch(x, y))
        #     time.sleep(0.8)
        #     print(swipe_screen(300, 300, 100, 100))
        #     flag = 0
        else:
            print(touch(x, y))
        wait = random.random() + 0.5  # 停0~9秒 指数越高平均间隔越短
        print(wait)
        time.sleep(wait)
        print(count)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        os.system('adb kill-server')
        print('bye')
        exit(0)


# TODO: 过程中要添加随机点击-OK
# TODO：寻找LV小怪的时候随机指数要反向写-CANCEL
# TODO：改善找到boss后要经过多次点击进入boss,战斗过程中程序失败-to do
# TODO: 改为三通道匹配-CANCEL
# TODO: 决策时间太慢了，boss与小怪的匹配程度太低了-OK
# TODO: 增加滑动屏幕更改地图位置功能-OK
# TODO: 增加统计战利品功能
# TODO: 改善现有的boss数量统计功能
# TODO: 根据实际情况滑动地图，因为地图并不是在右下角总有敌人
