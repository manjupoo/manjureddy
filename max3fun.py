def max(m,n,o):
	if m>n and n>o:
		print(m,"is larger then n")
	elif n>o and o>m:
		print(n,"is larger then o")
	else:
		print(o,"is larger then m and n")

print ("enter three values")
m=input()
n=input()
o=input()
max(m,n,o)
