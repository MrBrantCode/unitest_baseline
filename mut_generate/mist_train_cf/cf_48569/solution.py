"""
QUESTION:
Write a function named `change` that takes one argument `test`. The function should return a string message based on the value of `test`. The function should handle both integers and floating numbers. If `test` is not an integer or float, return "Invalid type". If `test` is greater than 1000, return "Value is too high". If `test` is greater than 10 but not greater than 1000, return "Value is above 10". Otherwise, return "Value is equal or below 10".
"""

def change(test):
  if isinstance(test, int) or isinstance(test, float):
    if test > 1000:
       return 'Value is too high'
    elif test > 10:
       return 'Value is above 10'
    else:
       return 'Value is equal or below 10'
  else:
    return "Invalid type"