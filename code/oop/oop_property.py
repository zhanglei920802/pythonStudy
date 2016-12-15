#!/usr/bin/env python2.7
#coding:utf-8
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


student = Student();
student.birth = 2005;
print(student.age);