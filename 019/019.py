'''
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
程序分析：请参照程序Python 练习实例14。
'''

import functools

def Divisor(x):
	list = []
	for i in range(1, x):
		if x % i == 0:
			list.append(i)
	return list

print("1000以内的所有完数:")
	
for i in range(2, 1001):
	if i == functools.reduce(lambda x, y : x+y, Divisor(i)):
		print("%d\t它的因子为%s" %(i, Divisor(i)))
