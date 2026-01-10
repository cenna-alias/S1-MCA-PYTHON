# Store a list of colors entered by the user. Display the first and last colors.

colors = input("Enter colors separated by commas:").split(",")
print(colors)
print("First color:",colors[0])
print("Last color:",colors[-1])
