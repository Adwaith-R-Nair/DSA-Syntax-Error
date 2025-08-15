a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
x, y = a, b
while y != 0:
    temp = y
    y = x % y
    x = temp
print("HCF:", x)