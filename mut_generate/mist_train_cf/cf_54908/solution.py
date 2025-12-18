"""
QUESTION:
Create a function `calculate(expression, x)` that evaluates a given mathematical expression at a given value of `x`. The function should handle the expressions `(x-1)^2`, `1/x`, and `sqrt(x)`. It should also handle edge cases such as division by zero and square root of negative numbers. If the given expression is not recognized, the function should return an error message.
"""

import math

def calculate(expression, x):
  if expression == "(x-1)^2":
    return (x-1)**2
  elif expression == "1/x":
    if x != 0:
      return 1/x
    else:
      return "Error: Division by zero."
  elif expression == "sqrt(x)":
    if x >= 0:
      return math.sqrt(x)
    else:
      return "Error: No square root for negative numbers."
  else:
    return "Error: Expression not recognized."