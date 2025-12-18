"""
QUESTION:
Create a recursive function `fibonacci(n)` that calculates the nth number in the Fibonacci sequence. The function should use recursion to find the sum of the two preceding numbers in the sequence. The function should handle the base cases where `n` equals 0 or 1. The function should not use any iterative methods, such as loops or arrays, to store previous Fibonacci numbers.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)