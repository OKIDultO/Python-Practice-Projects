'''
题目：判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 
'''

import math

list = []

for i in range(101, 201):
	list.append(i)
	for j in range(2, int(math.sqrt(i)+1)):
		if i % j == 0:
			list.pop()
			break
	
print("一共有%d个素数。\n他们分别是：%s" %(len(list), list))
