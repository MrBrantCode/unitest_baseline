"""
QUESTION:
Write a function `sum_excluding_divisible_by_3_or_5(n)` that calculates the sum of all numbers from 1 to `n`, excluding any number that is divisible by 3 or 5. The function should take an integer `n` as input and return the calculated sum.
"""

def sum_excluding_divisible_by_3_or_5(n):
    total = 0
    for i in range(1, n + 1):
        if i % 3 != 0 and i % 5 != 0:
            total += i
    return total