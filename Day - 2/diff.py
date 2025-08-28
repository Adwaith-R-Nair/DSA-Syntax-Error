# Leetcode 1281

def subtractProductAndSum(n):
    s = 0
    p = 1
    while n:
        digit = n % 10
        s += digit
        p *= digit
        n //= 10
    return p - s