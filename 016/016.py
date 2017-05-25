'''
题目：输出今天日期。
程序分析：使用 datetime 模块。
'''

import datetime

print(datetime.date.today().strftime('%m/%d/%Y'))
