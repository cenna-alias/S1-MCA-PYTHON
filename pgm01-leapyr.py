# Using while loop

start = int(input("Enter start year:"))
end = int(input("Enter end year:"))
while start <= end:
    if (start % 400 == 0) or (start % 4 == 0 and start % 100 != 0):
        print(start)
    start += 1

# Using for loop

start = int(input("Enter start year:"))
end = int(input("Enter end year:"))
for year in range(start, end + 1):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year)
