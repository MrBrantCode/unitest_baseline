"""
QUESTION:
Write a function called `sum_excluding_multiples` that calculates the sum of all integers from 0 to a given number `n`, excluding any multiples of a given number `multiple`. The function should take two parameters: `n` and `multiple`.
"""

def sum_excluding_multiples(n, multiple):
    return sum(i for i in range(n + 1) if i % multiple != 0)