import random

while True:
		d=input("press r to roll and q to quit")
		if d=="r":
		 	print("You got: ",random.randint(1,6))
		if d=="q":
		 	print("Bye!")
		 	exit()

print("end")
