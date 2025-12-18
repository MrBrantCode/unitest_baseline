"""
QUESTION:
Write a function `sum_numbers` that calculates the sum of all numbers from 1 to `n`, excluding numbers that are divisible by both 3 and 5. The function should only use a single loop and not utilize any built-in functions or libraries for mathematical calculations.
"""

def sum_numbers(n):
    total = 0
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            continue
        total += i
    return total