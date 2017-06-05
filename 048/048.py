'''
题目：数字比较。
程序分析：无
'''

compare = []

x = compare.append(int(input("请输入一个数：")))
y = compare.append(int(input("再输入一个数：")))

compare.sort()

print("较大的数为：%d\n较小的数为：%d" %(compare[1], compare[0]))
