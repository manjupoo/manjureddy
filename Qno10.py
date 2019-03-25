#wap to take three number from user and return their sum,return 0 if any of the two numbers are equal
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 = int(input("Enter 3rd number: "))
sum = n1+n2+n3
print("sum ",sum)
if n1==n2 or n2==n3 or n3==n1:
	print("0")