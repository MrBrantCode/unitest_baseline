"""
QUESTION:
Write a function `sumOfOddNumbers` that takes two integers `lower` and `upper` as input and returns the sum of all odd numbers between `lower` and `upper` (inclusive).
"""

def sumOfOddNumbers(lower, upper):
    total = 0
    for i in range(lower, upper+1): 
        if (i % 2 != 0): 
            total += i
    return total