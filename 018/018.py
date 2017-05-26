'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
程序分析：关键是计算出每一项的值。
'''

import functools

def Number():
	for i in range(x):
		num.append(int(str(a) * (i+1)))
	return num

num = []
a = int(input("循环数："))
x = int(input("相加数个数："))

#reduce() & lambda()函数
sum = functools.reduce(lambda x, y : x+y, Number())

print(num[0], end = "")
for i in range(1, x):
	print(" + %d" %num[i], end = "")
print(" = %d" %sum)
