'''
题目：对10个数进行排序。
程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。
'''

def Rank(l, x):
	for i in range(x, len(l)):
		if l[x] > l[i]:
			l[x],l[i] = l[i],l[x]
	print(l[x], end = "  ")

l = []

print("请输入10个数字：")

for i in range(10):
	l.append(int(input()))

print("排序结果：")

for j in range(len(l)):
	Rank(l, j)
