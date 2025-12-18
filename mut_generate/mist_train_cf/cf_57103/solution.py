"""
QUESTION:
Create a function `power(n, m)` that calculates the value of `n` raised to the power of `m` without using the direct exponentiation operator or looping constructs. The function should handle integer values of `m`, including 0.
"""

def power(n, m):
    if m == 0:
        return 1
    elif m % 2 == 0:
        return power(n * n, m // 2)
    else:
        return n * power(n * n, (m - 1) // 2)