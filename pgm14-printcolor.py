# Print the colors from list1 that are not present in list2.

# Using list comprehension

list1 = ["Red","Green","Blue","White"]
list2 = ["Green","White"]
print(list1)
print(list2)
result = [c for c in list1 if c not in list2]
print("Colors not in list2:",result)

# Using for loop

list1 = ["Red", "Green", "Blue", "White"]
list2 = ["Green", "White"]
print(list1)
print(list2)

result = []
for color in list1:
    if color not in list2:
        result.append(color)

print("Colors not in list2:", result)
 