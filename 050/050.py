'''
题目：输出一个随机数。
程序分析：使用 random 模块。
'''

import random

print(random.random())           #输入0-1之间的随机数
print(random.uniform(10,20))     #输出10-20之间的随机数
print(random.randint(10,20))     #输出10-20之间的随机整数
