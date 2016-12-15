#!/usr/bin/env python2.7
#coding:utf-8
#记录模块
import logging;
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')


try:
	print("try...");
	r = 10 / int('a');
	print('result:',r);
except ValueError as e:
	print("ValueError:",e);
except ZeroDivisionError as e:
	print("ZeroDivisionError:",e);
	#使用日志记录
	logging.exception(e);
else:
	print("no error");
finally:
	print("finally");
print("END");


# err_raise.py
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
    	#抛出异常
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')