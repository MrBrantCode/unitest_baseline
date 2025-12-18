"""
QUESTION:
Create a function called `sum_even_numbers(n)` that calculates the sum of all even numbers from 1 to `n` (inclusive). The function should take an integer `n` as input and return the sum of all even numbers within the given range.
"""

def sum_even_numbers(n):
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum += i
    return sum