"""
QUESTION:
Design a function named `sum_divisibles(n)` that calculates the sum of all numbers between 2 and `n` (inclusive) that are divisible by either 2 or 5. The function should take an integer `n` as input and return the calculated sum.
"""

def sum_divisibles(n):
    sum_total = 0
    for i in range(2, n+1):
        if i % 2 == 0 or i % 5 == 0:
            sum_total += i
    return sum_total