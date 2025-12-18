"""
QUESTION:
Create a function called `is_perfect_square(n)` that takes a positive integer `n` as input. The function should return the integer square root of `n` if `n` is a perfect square; otherwise, it should return `False`.
"""

import math

def is_perfect_square(n):
  root = math.sqrt(n)
  if int(root + 0.5) ** 2 == n:
    return int(root)
  else:
    return False