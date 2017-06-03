'''
题目：求一个3*3矩阵对角线元素之和。
程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
'''

l = [[], [], []]
sum = 0

print("输入3*3矩阵中数据：")

for i in range(3):
	for j in range(3):
		l[i].append(int(input()))
		 
		if i == j:
			sum += l[i][j]

print("3*3矩阵:")
	
for i in range(3):	
	print(l[i])		

print("对角线元素之和为%d" %sum)
