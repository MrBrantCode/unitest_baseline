"""
QUESTION:
Write a recursive function `fibonacci(n)` that calculates the Fibonacci number at index `n`. The function should use recursive calls to compute the Fibonacci number. The Fibonacci sequence is defined such that each number is the sum of the two preceding ones, starting from 0 and 1.
"""

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)