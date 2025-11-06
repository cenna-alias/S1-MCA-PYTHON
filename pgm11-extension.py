file_name=input("Enter file name:")
if '.' in file_name:
	extension=file_name.split('.')[-1]
	print("File extension is:",extension)
else:
	print("No extension found in the file name")
