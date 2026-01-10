list1 = [int(x) for x in input("Enter list of integers:").split()]
print(list1)
list2 = [int(x) for x in input("Enter list of integers:").split()]
print(list2)

if len(list1) == len(list2):
	print("Same length")
else:
	print("Not the same length")

if sum(list1) == sum(list2):
	print("Same sum",sum(list1))
else:
	print("Different sum list1:",sum(list1),"list2:",sum(list2))
	
common_elements = set(list1).intersection(list2)
if common_elements:
	print("have same elements:",common_elements)
else:
	print("don't have same elements")
