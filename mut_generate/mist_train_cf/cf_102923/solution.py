"""
QUESTION:
Write a function `power_of_two` that calculates the value of 2 raised to a given power, without using any mathematical operators or built-in functions for exponentiation. The function should take an integer `n` as input and return the calculated value.
"""

def power_of_two(n):
    result = 1
    for _ in range(n):
        result *= 2
    return result