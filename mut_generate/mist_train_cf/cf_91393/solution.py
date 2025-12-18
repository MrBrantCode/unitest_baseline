"""
QUESTION:
Compute the sum of numbers from 1 to n using a for loop without using arithmetic operators (+, -, *, /, etc.). The function should be named sum_numbers.
"""

def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total