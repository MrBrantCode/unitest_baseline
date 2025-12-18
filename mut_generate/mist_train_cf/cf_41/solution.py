"""
QUESTION:
Implement a function called `fibonacci` that takes an integer `n` as input and returns the nth Fibonacci number using a recursive approach. The function should have a time complexity of O(2^n) and should not use any built-in mathematical functions or libraries. Handle base cases where `n` is 0 or 1, and for `n` greater than 1, calculate the Fibonacci number as the sum of the two preceding numbers in the sequence.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)