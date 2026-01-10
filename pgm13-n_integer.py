# Calculate the value of n + nn + nnn where n is an integer input by the user.

n = int(input("Enter a number:"))
result = n + int(str(n)*2) + int(str(n)*3)
print("Result:",result)
