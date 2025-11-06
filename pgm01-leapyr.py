end = int(input("Enter end year:"))
start = int(input("Enter start year:"))
while(start<=end):
	if(start%400==0) or (start%4==0 and start%100!=0):
		print(start)
		start=start+1
	else:
		start=start+1
