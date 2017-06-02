'''
题目：求100之内的素数。
程序分析：无。
'''

print("100之内的素数:")

for i in range(2, 101):
	for j in range(2, i):
		if i % j == 0:
			break
	else:
		print(i)
