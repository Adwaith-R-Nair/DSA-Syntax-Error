"""
Brute Force Prime Check
Time Complexity: O(n)
Space Complexity: O(1)
"""

n = int(input("Enter a number: "))
is_prime = True
if n <= 1:
    is_prime = False # Numbers <= 1 are not prime
else:
    for i in range(2, n):
        if n % i == 0: # Found a divisor
            is_prime = False
            break
if is_prime:
    print("Prime")
else:
    print("Not Prime")