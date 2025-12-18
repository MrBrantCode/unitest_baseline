"""
QUESTION:
Calculate the result of 2 raised to the power of n without using any mathematical operations or built-in functions for exponentiation. The function should have a time complexity of O(log n) and a space complexity of O(1), where n is a positive integer less than or equal to 1,000. Implement the function `power_of_two(n)`.
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