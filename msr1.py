import random
#This ia dictionary
d={8:55,10:30,25:2,30:50,40:20,50:25,88:66,95:10}
p=random.choice([2,5,21,26,87])
print ("You got",p)
if p in d:
	if p>d[p]:
		print("Snake")
	else:
		print("Lader")
		print("Lou can go to",d[p])