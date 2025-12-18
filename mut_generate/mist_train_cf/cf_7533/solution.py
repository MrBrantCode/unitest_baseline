"""
QUESTION:
Write a function `power_of_two(n)` that calculates the result of 2 raised to the power of `n`, where `n` is a positive integer less than or equal to 1000. The function should not use any mathematical operations or built-in functions for exponentiation and should achieve a time complexity of O(log n) and a space complexity of O(1).
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