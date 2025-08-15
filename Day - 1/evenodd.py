"""
--------------------------------------------------------------
Approach                | Time Complexity | Space Complexity
--------------------------------------------------------------
1. Modulus Operator (%) | O(1)            | O(1)
2. Bitwise AND (&)      | O(1)            | O(1)
3. Subtract 2 Loop      | O(n)            | O(1)
4. Divide & Multiply    | O(1)            | O(1)
--------------------------------------------------------------
"""

n = int(input("Enter a number: "))

# 1. Modulus Operator
if n % 2 == 0:
    print("Using Modulus Operator: Even")
else:
    print("Using Modulus Operator: Odd")

# 2. Bitwise AND
if (n & 1) == 0:
    print("Using Bitwise AND: Even")
else:
    print("Using Bitwise AND: Odd")

# 3. Subtract 2 Loop
temp = abs(n)
while temp > 1:
    temp -= 2
if temp == 0:
    print("Using Subtract 2 Loop: Even")
else:
    print("Using Subtract 2 Loop: Odd")

# 4. Divide & Multiply
half = n // 2
if half * 2 == n:
    print("Using Divide & Multiply: Even")
else:
    print("Using Divide & Multiply: Odd")
