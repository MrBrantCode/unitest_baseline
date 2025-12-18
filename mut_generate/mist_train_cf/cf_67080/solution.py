"""
QUESTION:
Write a function `check_progression` that takes a list of numbers as input and returns `True` if the numbers are in strictly ascending order and `False` otherwise. The list must contain at least two elements.
"""

def check_progression(lst):
  for i in range(len(lst) - 1):
    if lst[i + 1] <= lst[i]:
      return False
  return True