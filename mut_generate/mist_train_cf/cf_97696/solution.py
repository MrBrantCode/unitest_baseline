"""
QUESTION:
Write a function `sum_even_numbers` that calculates the sum of even numbers in a sequence of the first n positive integers. The function should take an integer `n` as input and return the sum of even numbers from 1 to `n` (inclusive).
"""

def sum_even_numbers(n):
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum += i
    return sum