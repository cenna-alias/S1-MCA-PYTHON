start = int(input("Enter start of range:"))
end = int(input("Enter end of range:"))
result = []
for i in range(start,end+1):
	if int(i**0.5)**2==i:
		digits = str(i)
		if all(int(d) % 2 == 0 for d in digits):
			result.append(i)
print("Numbers:",result)

