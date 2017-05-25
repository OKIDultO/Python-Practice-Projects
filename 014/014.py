'''
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
'''

#求最小质数k
def Pri_Num(x):
	for k in range(2, int(x+1)):
		if x % k == 0:
			break
	return k

#分解质因数
def Number(x):
	if Pri_Num(x) == x:
		print(int(x))
	else :
		print("%d * " %Pri_Num(x), end = "")
		return Number(x/Pri_Num(x))		

x = int(input("请输入一个正整数："))
print("分解质因数结果为：%d = " %x, end = "")
Number(x)
