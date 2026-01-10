names = input("Enter first names:").split()
print(names)
count = 0
for name in names:
	count += name.count('a')
print("Occurrence of a in the list is:", count)
