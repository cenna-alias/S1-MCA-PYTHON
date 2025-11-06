integers = input("Enter integers:").split()
print(integers)
newList=[]
for num in integers:
	if int (num)>100:
		newList.append("Over")
	else:
		newList.append(num)
print(newList)
