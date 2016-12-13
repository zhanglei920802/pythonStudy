#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Aniamal(object):
	
	def __init__(self):
		pass

	def run(self):
		print("run called");

class Cat(Aniamal):
	pass

class Dog(Aniamal):
	pass


dog = Dog();
dog.run();
cat = Cat();
cat.run();

#获取对象类型
print(type(dog));
print(abs);

#使用isinsrtance();
#判断是否是列表中的一种
print(isinstance([1, 2, 3], (list, tuple)));


#使用dir
#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
dir('abc');
#判断对象是否存在属性？
hasattr(obj, 'x')
#获取对象属性
getattr(obj, 'z') # 获取属性'z'