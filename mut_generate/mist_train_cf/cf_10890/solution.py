"""
QUESTION:
Create a function named `sum_of_squares` that takes an integer `n` as input and returns the sum of the squares of all numbers between 1 and `n` (inclusive), excluding any multiples of 3.
"""

def sum_of_squares(n):
    total = 0
    for i in range(1, n+1):
        if i % 3 != 0:
            total += i**2
    return total