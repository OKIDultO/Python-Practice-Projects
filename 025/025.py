'''
题目：求1+2!+3!+...+20!的和。
程序分析：此程序只是把累加变成了累乘。
'''

product = 1
sum = 0

for i in range(1, 21):
	product *= i
	sum += product
	
print("1+2!+3!+...+20!的和为%d" %sum)
