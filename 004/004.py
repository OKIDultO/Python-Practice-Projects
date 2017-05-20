'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天。
'''

counter = 0

year = int(input('請輸入年份：'))
month = int(input('請輸入月份：'))
day = int(input('請輸入日期：'))

days_a_month = [31, 28, 31, 30 ,31, 30, 31, 31, 30, 31, 30, 31]
for i in range(month-1):
	counter += days_a_month[i]

#閏年判斷
if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) and (month > 2):
	counter += 1

counter += day

print('這是本年的第%d天' %counter)
