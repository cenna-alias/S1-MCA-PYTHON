str=input("Enter the string:")
print(str)

first_char = str[0]
result = first_char + str[1:].replace(first_char,'$')
print(result)
