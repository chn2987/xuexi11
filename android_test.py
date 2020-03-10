# -*- coding: utf-8 -*-
import os,time
a=1
while True:
    if a >3000:
        exit()
    time.sleep(7)
    print('第{}次滑动'.format(a))
    os.system('adb -s ea91a8e0 shell input swipe 540 1700 540 900 100')
    #os.system('adb -s PJQDU16105009881 shell input swipe 540 1200 540 700 100')
    a+=1
