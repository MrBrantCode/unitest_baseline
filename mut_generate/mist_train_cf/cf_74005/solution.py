"""
QUESTION:
Create a function `is_power_of_two(n)` that determines if a given positive integer `n` is an exponent of the base number two. The function should return `True` if `n` is a power of two, and `False` otherwise. The function should be optimized to work efficiently with very large numbers.
"""

def is_power_of_two(n):
  if n <= 0:
    return False
  else:
    return (n & (n-1)) == 0