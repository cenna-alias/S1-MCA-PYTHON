text = input("Enter the string:")
print(text)

first_char = text[0]
result = first_char + text[1:].replace(first_char,'$')
print(result)
