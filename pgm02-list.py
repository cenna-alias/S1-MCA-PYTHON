# To perform list manipulations using python list comprehensions and built-in functions.

# generate positive list of numbers from a given list of integers
numbers = [1, 2, -34, 34, 56, 100, -35]
for i in numbers:
	if i > 0:
		print(i)

# square of n numbers
numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
	print(i * i)
	
# form a list of vowels selected from a given text	
text = "Master of Computer Applications"
vowel_list = []
vowels = "aeiouAEIOU"
for i in text:
	if i in vowels:
		vowel_list.append(i)
print(vowel_list)

# list ordinal value of each element
print(ord('1'))
print(ord('0'))
