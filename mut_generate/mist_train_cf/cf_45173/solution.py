"""
QUESTION:
Design a recursive function named `fibonacci(n)` that calculates the nth Fibonacci number, where the Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, starting with 0 and 1. The function should successfully handle a maximum recursion depth of 15.
"""

def fibonacci(n):
  # Establish the base cases
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    # Recurse on the previous two Fibonacci numbers
    return fibonacci(n-1) + fibonacci(n-2)