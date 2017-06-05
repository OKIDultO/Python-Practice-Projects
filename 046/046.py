'''
题目：求输入数字的平方，如果平方运算后小于 50 则退出。
程序分析：无
'''

import math

x = 8

while math.pow(x, 2) >= 50:
	x = int(input("请输入一个数："))
	print("数字的平方为：%d" %math.pow(x, 2))
