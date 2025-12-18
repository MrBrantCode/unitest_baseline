"""
QUESTION:
Create a function named `sum_of_preceding_numbers` that takes a single integer `n` as input and returns the sum of all preceding numbers from 1 to `n-1` using recursion. The input number `n` must meet the following conditions: `n` is a prime number, `n` is divisible by 3, `n` is greater than 1 and less than 100, and `n` does not contain the digit 9.
"""

def sum_of_preceding_numbers(n):
    if n == 1:
        return 0
    return n + sum_of_preceding_numbers(n - 1)