#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#__________________判断输入数据的类型________________________
a=input('请输入数据')
print(type(a))#打印数据类型

if isinstance(a,str):
    print('变量a的类型为str')
    if a.isalpha():
        pass


