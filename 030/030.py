'''
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
程序分析：无。
'''

x = input("请输入一个五位数：")

list = list(x)

for i in range(len(list)):
	if list[i] != list[len(list)- i -1]:
		print("不", end = "")
		break

print("是回文数")
