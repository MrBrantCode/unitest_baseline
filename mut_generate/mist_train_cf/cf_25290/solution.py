"""
QUESTION:
Create a function named `fibonacci(n)` that calculates the nth Fibonacci number. The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1. The function should take an integer `n` as input and return the corresponding Fibonacci number. The function should be able to handle inputs where `n` is 0 or 1, returning `n` in these cases.
"""

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)