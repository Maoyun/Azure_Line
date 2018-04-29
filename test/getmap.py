# !/usr/bin/env python
# -*-coding:utf-8 -*-
# author:Dra Date：2018/4/26

import os

os.system('adb shell screencap -p /sdcard/autoAzure_line.png')
os.system('adb pull /sdcard/autoAzure_line.png F:/PycharmProject/Azure_Line/test')
