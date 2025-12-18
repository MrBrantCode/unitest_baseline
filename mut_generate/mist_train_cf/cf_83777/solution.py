"""
QUESTION:
Write a function `find_x` that calculates the value of 'x' in the equation x + 2.7 = 8.4 by subtracting 2.7 from both sides and returns the corresponding option from a given set of numerical values. The function should take a list of options as input and return the correct option.
"""

def find_x(options):
  result = 8.4 - 2.7
  for option in options:
    if abs(option + 2.7 - result) < 1e-9: # using the precision up to 9 decimal places
      return option