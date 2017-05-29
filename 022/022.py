'''
题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
'''

battle1 = ["a"]
battle2 = ["b"]
battle3 = ["c"]
team2 = ["x", "y", "z"]

for i in range(3):
	if team2[i] != "x" and team2[i] != "z":
		battle3.append(team2[i])
		team2.remove(team2[i])
		break

for j in range(2):
	if team2[i] != "x":
		battle1.append(team2[i])
		team2.remove(team2[i])
		break
		
battle2.append(team2[0])

print(battle1, battle2, battle3)
