#!/usr/bin/env python2.7
#coding:utf-8
#文件的读写

#使用StringIO
#from io import StringIO
#f = StringIO()
#f.write('hello')
#f.write("hello");
#f.write(" ");
#f.write("wolrd!");
#print(f.getvalue());

#byteio
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))