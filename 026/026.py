'''
题目：利用递归方法求5!。
程序分析：递归公式：fn=fn_1*4!
'''

def Pro_Ope(x):
	if x == 1:
		return 1
	else:
		return x * Pro_Ope(x-1)

print("5! = %d" %Pro_Ope(5))
