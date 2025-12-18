"""
QUESTION:
Write a function `check_even(number)` that takes an integer `number` as input and returns `True` if the number is even, and `False` otherwise. The function should use a Boolean flag to determine whether the number is even. The flag should initially be set to `False` and updated to `True` if the number is even.
"""

def check_even(number):
  flag = False
  if number % 2 == 0:
    flag = True
  return flag