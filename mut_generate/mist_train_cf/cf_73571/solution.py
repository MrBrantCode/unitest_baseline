"""
QUESTION:
Write a function `calculate_sum` that calculates the aggregate sum total of the cubed values of each individual integer from 1 up to and inclusive of a given endpoint `n`. The function should accept an integer `n` and return the calculated sum.
"""

def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 3
    return total