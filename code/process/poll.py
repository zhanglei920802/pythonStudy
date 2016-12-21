#!/usr/bin/env python2.7
#coding:utf-8
#创建进程池

from multiprocessing import Pool
import os, time,random;

def long_time_task(name):
	print("Run task %s [%s]...\n"%(name,os.getpid()))
	start = time.time();
	time = time.sleep(random.random() * 3);
	end = time.time();
	print("Task %s run %0.2f seconds.\n"%(name,(end - start)))

if __name__ == '__main__':
	print("Parent process %s.\n"%os.getpid());
	p = Pool(4);
	for i in range(5):
		p.apply_async(long_time_task,args=(i,));
	print("Waiting for all subprocess done\n");
	p.close();
	p.join();
	print("All subprocess done\n");