t = int(input("Enter no. of testcases- "))
for i in range(t):
	a = int(input())
	b = int(input())
	if(a > b):
		print(">")
	elif(a < b):
		print("<")
	elif(a == b):
		print("=")