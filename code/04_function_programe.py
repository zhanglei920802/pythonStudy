#!/usr/bin/env python2.7
#coding:utf-8
#传入函数

def add(x,y,f):
	return f(x) + f(y);

print(add(-4,5,abs));

#map/reduce
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
#http://research.google.com/archive/mapreduce.html
def f(x):
	return x*x;

L = range(1,10);
#print(L);
r = map(f,L);
print(r);

#再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce;

def add(x,y):
	return x + y;

result = reduce(add,[1,3,5,7,9]);
print(result);


#filter
#和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
	return n % 2 == 1;

print(filter(is_odd,[1,2,4,5,6,9,10,15]));

#去掉非空字符
def  not_empty(s):
	return s and s.strip();

print(filter(not_empty,['A','','B','None','C',' ']));



#排序
print(sorted([36, 5, -12, 9, -21]));
print(sorted([36, 5, -12, 9, -21], key=abs));


#返回函数
#求和函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

#而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

#当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
print(lazy_sum(1, 3, 5, 7, 9));

#调用函数f时，才真正计算求和的结果：
#print(f());
#请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1==f2);











