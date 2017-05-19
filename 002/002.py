'''
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
'''

profit = int(input('請輸入利潤（萬元）：'))

#定義利潤分段數組為i
i = [100, 60, 40, 20, 10, 0]
#定義提成率分段數組為r
r = [1, 1.5, 3, 5, 7.5, 10]

bonus = 0

for x in range(6):
	if profit > i[x]:
		bonus += (profit - i[x]) * r[x] / 100
		profit = i[x]
	
print('獎金（萬元）：%f' %bonus)