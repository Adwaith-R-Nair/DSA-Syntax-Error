n = int(input("Enter a number: "))
n = abs(n) # handle negative numbers
for i in range(n // 2):
    n -= 2
if n == 0:
    print("Even")
else:
    print("Odd")