# Calculate the GCD and LCM of two numbers.

a =int(input("Enter first number:"))
b =int(input("Enter second number:"))
x,y = a,b
while y!=0:
	x,y = y,x%y
gcd=x
lcm=abs(a*b)//gcd
print("GCD is:",gcd)
print("LCM is:",lcm)

# Using function

def gcd_lcm(a, b):
    x, y = a, b
    while y != 0:
        x, y = y, x % y
    gcd = x
    lcm = abs(a*b)//gcd
    return gcd, lcm

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
gcd, lcm = gcd_lcm(a, b)
print("GCD is:", gcd)
print("LCM is:", lcm)
