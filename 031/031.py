'''
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。
'''

x = input("判断星期几（首字母大写）\n请输入第一个字母:")

if x == "M":
	print("星期一")
elif x == "T":
	y = input("请输入第二个字母:")
	if y == "u":
		print("星期二")
	elif y == "h":
		print("星期四")
	else:
		print("输入有误！")
elif x == "W":
	print("星期三")
elif x == "F":
	print("星期五")
elif x == "S":
	y = input("请输入第二个字母:")
	if y == "a":
		print("星期六")
	elif y == "u":
		print("星期日")
	else:
		print("输入有误！")
else:
	print("输入有误！")
