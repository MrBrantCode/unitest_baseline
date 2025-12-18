"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given positive integer `n`. The function should return an error message if `n` is a non-positive integer or if the calculation results in an integer overflow.
"""

import math
import sys

def factorial(n):
  try:
    if n <= 0:
      return 'Error: input should be a positive integer'
    else:
      result = math.factorial(n)
      return result
  except OverflowError:
    return 'Error: integer overflow'
  except:
    return 'Error: unexpected error'