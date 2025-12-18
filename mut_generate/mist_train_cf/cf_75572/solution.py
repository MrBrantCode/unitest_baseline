"""
QUESTION:
Write a recursive function `factorial(n)` that calculates the factorial of a non-negative integer `n`. The function should return the product of all positive integers less than or equal to `n`. Assume `n` is a non-negative integer.
"""

def factorial(n):
  if n == 0:  # base case
     return 1
  else:
     return n * factorial(n-1)  # recursive call