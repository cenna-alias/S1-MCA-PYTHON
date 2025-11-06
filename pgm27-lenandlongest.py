words = input("Enter words separated by space:").split()
longest = max(words,key = len)
print("Longest word:",longest)
print("Length:",len(longest))
