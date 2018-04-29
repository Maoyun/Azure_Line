# !/usr/bin/env python
# -*-coding:utf-8 -*-
# author:Dra Date：2018/2/24

import cv2
import numpy as np


def match(img, model, value):  # 模板和查找目标
        # 加载原始图像(RGB)
        img_rgb = cv2.imread(img)
        # 创建原始图像的灰度版本，所有操作在灰度版本中处理，然后再RGB图像中使用相同坐标还原
        img_gray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
        # 加载将要搜索的图像模板
        tmp = cv2.imread(model,0)
        # 记录图像模板的尺寸
        w,h = tmp.shape[::-1]
        # 查找图像
        res = cv2.matchTemplate(img_gray, tmp, cv2.TM_CCOEFF_NORMED)
        # 设定阈值
        thread = value
        # res大于thread
        loc = np.where(res >= thread)
        px = loc[1]
        py = loc[0]
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(7,249,151),2)
        cv2.namedWindow('show',0)
        cv2.resizeWindow('show',960,540)
        cv2.moveWindow('show',960,540)
        cv2.imshow("show",img_rgb)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(px[0],py[0])


image = "autoAzure_line.png"
targets = "diren3.png"
value = 0.6
match(image, targets, value)