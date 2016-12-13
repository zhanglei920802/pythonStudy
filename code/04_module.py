#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#' a test module '
__author__='ZhangLei'
#类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名
#类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等
#定义为私有的函数
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
	return "Hello,%s" % name;

def greeting(name):
	if(len(name) > 3):
		return _private_1(name);
	else:
		return _private_2(name);

print(greeting("hello"))
#模块
#安装模块
#pip install Pillow
from Pillow import Image;
im = Image.open("test.png");
print(im.format,im.size,im.mode);
im.thumbnail(200,100);
im.save("test_thumbnail.jpg","JPEG");