"""
QUESTION:
Create a function `is_even(n)` and `is_odd(n)` that determines whether a given integer `n` is even or odd using mutual recursion. The function should return `True` if `n` is even and `False` if `n` is odd.
"""

def is_even(n):
  if n == 0:
    return True
  else:
    return is_odd(n-1)

def is_odd(n):
  if n == 0:
    return False
  else:
    return is_even(n-1)