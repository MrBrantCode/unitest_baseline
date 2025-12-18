"""
QUESTION:
Implement a function called `power_of_two` that calculates the result of raising 2 to the power of n, where n is an integer between 1 and 10^9. The function should have a time complexity of O(log n) and should not use any built-in mathematical functions or operators for exponentiation.
"""

def power_of_two(n):
    result = 1
    base = 2

    while n > 0:
        if n % 2 == 1:
            result *= base
        base *= base
        n //= 2

    return result