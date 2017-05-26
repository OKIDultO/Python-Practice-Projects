'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析：利用while语句,条件为输入的字符不为'\n'。
'''

x = input("请输入字符：")

letters = 0
spaces = 0
digits = 0
others = 0

for i in x:
	if i.isalpha():	
		letters += 1
	elif i.isspace():
		spaces += 1
	elif i.isnumeric():
		digits += 1
	else:
		others += 1
	
print("统计结果：%s个英文字母，%s个空格，%s个数字，%s个其它字符" %(letters, spaces, digits, others))
