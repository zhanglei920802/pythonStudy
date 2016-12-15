#!/usr/bin/env python2.7
#coding:utf-8
#使用定制类
class Student(object):
	@property
	def birth(self):
		self._birth;

	@birth.setter
	def birth(self,value):
		self._birth = value;

	@property
	def age(self):
		return 2016 - self._birth;

	def __str__(self):
		return "age[%d]" % self.age;

student = Student();
student.birth = 1992;
print(student);


#iter
#class Fib(object):
#    def __init__(self):
#        self.a, self.b = 0, 1 # 初始化两个计数器a，b
#
#    def __iter__(self):
#        return self # 实例本身就是迭代对象，故返回自己
#
#    def __next__(self):
#        self.a, self.b = self.b, self.a + self.b # 计算下一个值
#        if self.a > 100000: # 退出循环的条件
#            raise StopIteration();
#        return self.a # 返回下一个值
# 	def __getitem__(self, n):
#        a, b = 1, 1
#        for x in range(n):
#            a, b = b, a + b
#        return a


 #使用枚举类
from enum import Enum

month = Enum("Month", ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'));
for name,member in month.__iter__.items():
	print("name[%s],member[%s]"%(name,member));
