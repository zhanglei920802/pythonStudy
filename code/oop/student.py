#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#定义类
#object表示从object继承
class Student(object):
	grade = "A";#增加属性
	#构造方法,第一个参数始终是self,表示创建的实例本身
	def __init__(self,name,score):
		#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，
		self.name = name;
		self.score = score;
		#私有变量
		#self.__name = name;
		#self.__score = score;

		#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
		#。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量
		#这是一个坑
	def print_score(self):
		print("name:%s,score:%s"%(self.name,self.score));



#使用
studentA = Student("ZhangSan",89);
studentA.grade = "B";
studentB = Student("Lisi",90);
studentA.print_score();
studentB.print_score();
print("grade:%s"%studentA.grade);