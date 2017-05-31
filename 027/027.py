'''
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
程序分析：无。
'''

def List(i):
	if i == 0:
		return list
	else:
		x = (input(""))
		list.insert(0, x)
		return List(i-1)

list = []
print("请输入5个字符：")
print("反序输出结果为：\n%s" %List(5))
