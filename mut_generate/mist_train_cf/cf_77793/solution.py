"""
QUESTION:
Create a function `mathematical_expression` that takes two double integers `x` and `y` as input and returns the result of the mathematical expression `x*x + y / (y**y) - (x * y)/y`. Ensure the operations are performed in the correct order using parentheses.
"""

def mathematical_expression(x, y):
    corrected = x*x + y / (y**y) - (x * y)/y 
    return corrected