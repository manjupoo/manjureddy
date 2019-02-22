import random
p=0
q=0

while true 
	r=input("press r to roll the dice : ")

	if r =="r":
		r = random.randint(1,6)
		print ("you got : ",d)
		if d==1 or d== 6 :
			p = d
			break

print("congratulations waste fellow you are in the game . you are at :", p)