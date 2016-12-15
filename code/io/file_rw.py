#!/usr/bin/env python2.7
#coding:utf-8
#文件的读写


#读取文件
f = open("test.txt","r");
print(f.read());
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉
f.close();

#with自动调用close方法
with open("test.txt","r") as f:
	print(f.read());


