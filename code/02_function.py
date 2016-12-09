#!/usr/bin/env python3
def my_abs(x):
	if x >= 0:
		return x;
	else:
		return -x;

print(my_abs(-6));


#位置参数
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

 #使用
print(5)
print(5,2)
#一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
#二是如何设置默认参数。
#当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')

#可变参数
def calc(*number):
	sum = 0;
	for n in number:
		sum = sum + n * n;
	return sum;

print(calc(1,2,3));
print(calc());
nums = [1, 2, 3];
print(nums);

#关键字参数
def person(name,age,**ky):
	print('name:',name,'age:',age,'other:',ky);

person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
#关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到

#命名关键字参数
#对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查


#递归函数
def fact(n):
	if n == 1:
			return 1;
	return n * fact(n-1);