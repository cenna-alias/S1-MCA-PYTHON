text = input("Enter the string:")
print(text)
c = dict()
words = text.split()
for i in words:
	if i in c:
		c[i]=c[i]+1
	else:
		c[i]=1
print(c)
