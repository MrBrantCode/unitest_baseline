"""
QUESTION:
Create a function named `is_odd` that takes one argument `x`. The function should return `True` if `x` is an odd integer, `False` if `x` is an even integer, and an error message if `x` is a non-integer. The function should not assume any specific input type and should handle both integer and non-integer inputs accordingly.
"""

def is_odd(x):
  if not isinstance(x, int):
    return "Error: Non-integer input"
  if x % 2 == 1:
    return True
  else:
    return False