"""
QUESTION:
Create a function `sum_numbers` that takes a positive integer as input and returns the sum of all positive integers from 1 to the given number. The function should not take any additional parameters and should only use the input number to calculate the sum.
"""

def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total