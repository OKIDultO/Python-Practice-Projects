'''
题目：按逗号分隔列表。
程序分析：无。
'''

list1 = input("请输入：")

list2 = "," .join(str(i) for i in list1)

print("逗号分隔:%s" %list2)
