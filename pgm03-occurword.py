str = input("Enter the string:")
print(str)
c = dict()
words = str.split()
for i in words:
	if i in c:
		c[i]=c[i]+1
	else:
		c[i]=1
print(c)
