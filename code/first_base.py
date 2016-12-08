#!/usr/bin/env python3
#coding=utf-8
print('Hello,python');

#python字符串
#用'或者"
print('I\'m Ok');


###############################布尔值
# True & False
print(True and False)
print(True or False)
print(5 > 3 and 3 > 1)
print( not 1 > 2)

age = 20;#声明一个int
t_007='T0007';#声明字符串
isTrue = True;#声明bool型
if age >= 18:
    print('adult')
else:
    print('teenager')

a = 'ABC'
b = a
a = 'XYZ'
print(b)

#常量
PI = 3.141592;



##################区分
print( 9 / 3)#
print(10//3)#地板除


#############################################字符串#############################
#现在，捋一捋ASCII编码和Unicode编码的区别：ASCII编码是1个字节，而Unicode编码通常是2个字节。

#字母A用ASCII编码是十进制的65，二进制的01000001；

#字符0用ASCII编码是十进制的48，二进制的00110000，注意字符'0'和整数0是不同的；

#汉字中已经超出了ASCII编码的范围，用Unicode编码是十进制的20013，二进制的01001110 00101101。

#你可以猜测，如果把ASCII编码的A用Unicode编码，只需要在前面补0就可以，因此，A的Unicode编码是00000000 01000001。

#新的问题又出现了：如果统一成Unicode编码，乱码问题从此消失了。但是，如果你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。

#所以，本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间：
#在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

#用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件：

#print('文')

#获取字符的整数表示
print(ord('A'));#65
#将编码转换为对应的字符
print(chr(66));#B
#print(chr(25931));#文
#print('\u4e2d\u6587')


#格式化
hello = 'Hello,%s'%'python';
#Hello,python
print(hello);
hello = 'Hell,%s.You Have $%d' %('Tom',10000);
print(hello);
#%的转义
hello =  'growth rate: %d %%' % 7;
print(hello);


############list&tuple
#classmates就是一个list
classmates = ['AA','BB','CC'];
print('len=[%d],data[%s]'%(len(classmates),classmates));

print('index[0]=%s,index[-1]=%s'%(classmates[0],classmates[-1]));

#追加一个元素
classmates.append('DD');
print(classmates);
#在指定位置插入一个元素
classmates.insert(1,'EE');
print(classmates);
#删除末尾元素
print(classmates.pop());
print(classmates);

#tuple元组
#tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
#声明一个元组
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
#tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比

t = (1)#表示1
t = (1,)#表示只有一个元素的元组

#条件判断
#if语句
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
#if else
age = 3;
if age >= 18:
	print('your age is ',age);
	print('Adult');
else:
	print('your age is ',age);
	print('teenager');

#if else if
if age >= 18:
	print('your age is ',age);
	print('Adult');
elif age>=6:
	print('your age is ',age);
	print('teenager');
else:
	print('your age is ',age);
	print('kid');
#if判断条件还可以简写，比如写：
#x是非零数值、非空字符串、非空list等，就判断为True，否则为False
if 200:
    print('True')


#s = input('birth: ')
s = 100;
birth = int(s);
#print('birth:',birth);

if birth < 2000:
    print('00before');
else:
    print('00 after');


###############循环
#for循环
for name in classmates:
	print(name);

sum = 0;
for x in [1,2,3,4,5,6,7,8,9]:
	sum += x;
print(sum);

#range(5)生成的序列是从0开始小于5的整数
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

#while循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)


#dict & set
#dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print('Michael');

#判断指定的key是否存在
print('Michael' in d);
#获取指定的key的value
print(d.get('Bob',-1));
#删除一个Key
print(d.pop('Bob'));

#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
#创建一个set
s = set([1, 2, 3]);
print(s);
 #重复元素将会被自动过滤
s = set([1, 1, 2, 2, 3, 3])
print(s);
#添加一个元素
s.add(4);
print(s);

#删除一个元素
s.remove(4);
print(s);


s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
#求交集
print(s1 & s2);
#求并集
print(s1 | s2);
#set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。
