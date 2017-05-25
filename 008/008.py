'''
题目：输出 9*9 乘法口诀表。
程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
'''

print("9*9 乘法口诀表：")

for i in range(1, 10):
	print()
	for j in range(1, i+1):
		print("%d * %d = %d\t" %(i, j, i*j), end="")