"""
QUESTION:
Write a function `factorial(x)` that calculates the factorial of a given positive integer `x`. The function should be able to handle a recursive call to calculate the factorial.
"""

def factorial(x):
  if x == 0:
    return 1
  else:
    return x * factorial(x-1)