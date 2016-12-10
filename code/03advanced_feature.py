#!/usr/bin/env python3

#切片

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

#常规方法
r = [];
n = 3;
for i in range(3):
	r.append(L[i]);

print(r);

#切片
print(L[:3]);#0,1,2
print(L[1:3]);#0,1
print(L[-1]);#最后一个元素


L = list(range(100))
print(L[:10]);#前10个数
print(L[-10]);#前10个数
print(L[10:20]);#11-20
print(L[:10:2]);#前10个数，没两个取一个
print(L[::5]);#每5个取一个


#迭代
d = {'a': 1, 'b': 2, 'c': 3};
for key in d:
	print(key);


from collections import Iterable
#判断是否是可迭代
print(isinstance('abc',Iterable));
print(isinstance([1,2,3],Iterable));
print(isinstance(123,Iterable));

#列表生成器
#生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))
print(list(range(1, 11)));
#生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L = [];
for x in range(1, 11):
	L.append(x * x);
print(L);

print([x * x for x in range(1, 11)]);
#偶数的平方
print([x * x for x in range(1, 11) if x % 2 == 0]);

import os ;# 导入os模块，模块的概念后面讲到
print([d for d in os.listdir('.')]);
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.items():
	print(k,'=',v);



#生成器
#在Python中，这种一边循环一边计算的机制，称为生成器：generator。

#创建一个列表
L = [x * x for x in range(10)]
print(L);

#创建生成器
#第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
g = (x * x for x in range(10))
#通过next打印
#每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
print(next(g));
print(next(g));
print(next(g));
print(next(g));

#斐波拉契数列，加了yield就成了generator了
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o = odd();
next(o);
next(o);
next(o);


#迭代器
#一类是集合数据类型，如list、tuple、dict、set、str等；
#一类是generator，包括生成器和带yield的generator function。
from collections import Iterable;
print(isinstance([],Iterable));