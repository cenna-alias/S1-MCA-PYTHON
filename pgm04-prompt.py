# Prompt the user for a list of integers.For all values greater than 100, store "Over" otherwise
# store the integer itself. 

integers = input("Enter integers:").split()
print(integers)
newList = []
for num in integers:
	if int (num)>100:
		newList.append("Over")
	else:
		newList.append(num)
print(newList)
