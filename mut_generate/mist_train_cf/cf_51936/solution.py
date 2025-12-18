"""
QUESTION:
Write a function `sum_odd_numbers(n)` to calculate the sum of all odd numbers up to a given non-negative integer `n`. Do not use any Python built-in functions or libraries for the task. The function should iterate over all integers from 0 to `n` inclusive, check if the current integer is odd, and add it to a running total.
"""

def sum_odd_numbers(n):  
    total = 0  
    for i in range(n + 1):  
        if i % 2 != 0:  
            total += i  
    return total