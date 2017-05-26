'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
程序分析：关键是计算出每一项的值。
'''

def Number(x):
	n = a
	while len(str(n)) < x:
		n = n * 10 + a
	return n

a = int(input("循环数："))
x = int(input("相加数个数："))
sum = 0

for i in range(x):
	print("%d" %Number(i+1), end = "")
	sum += Number(i+1)
	if (i + 1) < x:
		print(" + ", end = "")
	
print(" = %d" %sum)
