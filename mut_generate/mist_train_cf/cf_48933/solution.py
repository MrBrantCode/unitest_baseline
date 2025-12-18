"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given integer `n`. The function should return the product of all positive integers less than or equal to `n`. If `n` is 0 or 1, the function should return 1.
"""

def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    fact = 1
    for i in range(1, n+1):
      fact = fact * i
    return fact