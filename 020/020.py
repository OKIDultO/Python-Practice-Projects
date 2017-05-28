'''
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
程序分析：无
'''

height = 100
distance = 0
counter = 0

while counter <= 10:
	distance += height
	counter += 1
	height = height / 2
	
	if counter == 10:
		print("第10次落地时经过了%f米" %distance)
		print("第10次反弹%f米高" %height)
		
	distance += height
