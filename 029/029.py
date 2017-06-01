'''
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
程序分析：学会分解出每一位数。
'''

x = list(input("请输入一个不多于5位的正整数："))

print("它是%d位数" %len(x))
print("逆序打印：", end = "")

x.reverse()

for i in range(len(x)):
	print(x[i], end = "")
