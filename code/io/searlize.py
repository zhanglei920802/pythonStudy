#!/usr/bin/env python2.7
#coding:utf-8

#把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
import pickle
d = dict(name="bob",age=20,score=88);
print(pickle.dumps(d));

#序列化
f = open('dump.txt', 'wb');
pickle.dump(d, f);
f.close();

#反序列化
f = open("dump.txt","rb");
d = pickle.load(f);
f.close();
print(d);