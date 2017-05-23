'''
题目：暂停一秒输出，并格式化当前时间。
程序分析：无。
'''

import time

print(time.asctime(time.localtime(time.time())))

time.sleep(1)
print(time.asctime(time.localtime(time.time())))
