"""
QUESTION:
Implement a function named `calculate_gcd(a, b)` that calculates the greatest common factor of two positive integers `a` and `b` without using built-in functions or libraries for GCD calculation, and without using additional data structures or arrays. The function should run in O(sqrt(min(a, b))) time complexity.
"""

def calculate_gcd(a, b):
    if a < b:
        a, b = b, a

    gcd = b

    for i in range(1, int(b ** 0.5) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

        if a % (b // i) == 0 and b % (b // i) == 0:
            gcd = b // i

    return gcd