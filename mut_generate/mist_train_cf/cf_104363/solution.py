"""
QUESTION:
Implement a function named `gcd` that takes two integers `a` and `b` as input and returns their Greatest Common Divisor (GCD) without using any built-in functions or modules for calculating the GCD. The function should have a time complexity of O(log min(a, b)) and a space complexity of O(1).
"""

def gcd(a, b):
    # Check if either number is 0
    if a == 0:
        return b
    if b == 0:
        return a

    # Find the smaller number
    smaller = min(a, b)

    # Iterate from 1 to the smaller number
    for i in range(1, smaller + 1):
        # Check if both numbers are divisible by i
        if a % i == 0 and b % i == 0:
            gcd = i  # Update the gcd

    return gcd