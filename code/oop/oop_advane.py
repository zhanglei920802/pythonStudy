#!/usr/bin/env python2.7
#coding:utf-8

class Student(object):
    pass;

s = Student();
s.name = "Bob";#动态绑定一个属性
print(s.name);

#动态给实例增加一个函数
def set_age(self,age):
    self.age = age;

from types import MethodType;
s.set_age = MethodType(set_age,s);
s.set_age(25);
print(s.age);

s2 = Student();
#将会抛出异常
#s2.set_age(33);

#给类增加一个函数
def set_score(self,score):
    self.score = score;

Student.set_score = set_score;
s.set_score(100);
print(s.score);

#使用__slot__限制类的属性