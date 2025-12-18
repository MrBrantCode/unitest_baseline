"""
QUESTION:
Write a function `calculate_sum` that calculates the sum of all natural numbers from 1 to a given input number `n`. The function should return the calculated sum.
"""

def calculate_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum