#!/usr/bin/env python2.7
#coding:utf-8
import os

print("name:%s"%os.name);
print("uname:",os.uname());
print("env:",os.environ);
#获取java_home
print("javaHome:",os.environ.get("JAVA_HOME"));
print("path:",os.environ.get("PATH"));
#当前路径的绝对路径
print(os.path.abspath('.'));
#在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join('/Users/michael', 'testdir'));\
os.mkdir('/Users/michael/testdir');
os.rmdir('/Users/michael/testdir')