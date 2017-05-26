'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析：利用while语句,条件为输入的字符不为'\n'。
'''

x = str(input())

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = [0, 0, 0, 0]

for i in range(len(x)):
	if x[i] == " ":
		counter[1] = counter[1] + 1
	
	else:
		for j in range(len(letter)):
			if x[i] == letter[j]:
				counter[0] = counter[0] + 1
				break
		
		for k in range(len(number)):
			if x[i] == str(number[k]):
				counter[2] = counter[2] + 1
				break
		
counter[3] = len(x) - counter[0] - counter[1] - counter[2]
	
print("统计结果：%s个英文字母，%s个空格，%s个数字，%s个其它字符" %(counter[0], counter[1], counter[2], counter[3]))
