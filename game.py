import random
l=("paper","rock","scissor")
while True: 
	u=input("choose paper, rock, scissor")
	c=random.choice(l)
	print("you choose:",u,"amd computer choose",c)
	if u=="o":
		print("KEL KATHAM DHUKAN BHAND")
	elif c==u:
		print("draw match")
	elif u=="paper" and c=="rock":
		print("computer wins..!!!")
	elif u=="rock" and c=="scissor":
		print("you won..!!!")
	elif u=="scissor" and c=="paper":
		print("you won..!!!")
	elif u=="paper" and c=="scissor":
		print("comput won..!!!")
	elif u=="rock" and c=="paper":
		print("you won..!!!")
	elif u=="scissor" and c=="rock":
		print("computer won..!!!")