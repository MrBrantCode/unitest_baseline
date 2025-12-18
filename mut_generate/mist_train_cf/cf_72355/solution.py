"""
QUESTION:
Create a function `advanced_calculation(n)` that calculates the cumulative total of all numbers below `n` that contain the digit 5 and are divisible by either 9 or 12 without a remainder.
"""

def advanced_calculation(n: int) -> int:
    result = 0
    for i in range(5, n):
        if ('5' in str(i)) and ((i % 9 == 0) or (i % 12 == 0)):
            result += i
    return result