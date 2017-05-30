'''
题目：求1+2!+3!+...+20!的和。
程序分析：此程序只是把累加变成了累乘。
'''

def Pro_Ope(x):
	product = 1
	for i in range(2, x+1):
		product *= i
	return product
	
sum = 0
for i in range(1, 21):
	sum += Pro_Ope(i)
	
print("1+2!+3!+...+20!的和为%d" %sum)
