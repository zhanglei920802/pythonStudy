#!/usr/bin/env python2.7
#coding:utf-8
import logging;
#有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了
logging.basicConfig(level=logging.INFO);
def foo(s):
	n = int(s);
	print(n);
	#assert n!=0,'n is zero!';
	logging.info('n=%d',n);
	return 10/n;

#def main():
foo(0);

#pdb

s = '0'
n = int(s)
print(10 / n)