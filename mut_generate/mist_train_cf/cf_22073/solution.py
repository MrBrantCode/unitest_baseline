"""
QUESTION:
Write a function called `power_of_ten(n)` that calculates the result of 10 raised to the power of `n`, where `n` is a positive integer less than or equal to 100. The function should not use any built-in functions for exponentiation or mathematical operations for exponentiation and should have a time complexity of O(n) and a space complexity of O(1).
"""

def power_of_ten(n):
    result = 1
    for i in range(n):
        result *= 10
    return result