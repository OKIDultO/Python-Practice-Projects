'''
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
程序分析：请抓住分子与分母的变化规律。
'''

def Next_Num(x, i):
	x.append(x[-1] + x[-2])
	return x[i]

numerator = [2, 3]
denominator = [1, 2]
sum = 0

for i in range(20):
	if i < 2:
		sum += (numerator[i] / denominator[i])
	else:
		sum += (Next_Num(numerator, i) / Next_Num(denominator, i))
		
print("前20项之和为：%f" %sum)
