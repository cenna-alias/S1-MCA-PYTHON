list1 = ["Red","Green","Blue","White"]
list2 = ["Green","White"]
print(list1)
print(list2)
result = [c for c in list1 if c not in list2]
print("Colors not in list2:",result)
