"""
QUESTION:
Write a function called `sum_of_multiples` that calculates the sum of all numbers from 1 to n (inclusive) that are divisible by 3.
"""

def sum_of_multiples(n):
    total = 0
    for i in range(n + 1):
        if i % 3 == 0:
            total += i
    return total