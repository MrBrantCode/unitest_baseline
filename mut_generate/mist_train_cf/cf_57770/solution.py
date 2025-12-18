"""
QUESTION:
Write a function `solve_expression(expression)` that takes a string containing a mathematical expression and returns the result of the expression as a string, rounded to two decimal places. The expression can contain parentheses, addition (+), subtraction (-), division (/), and multiplication (*), and can include fractional numbers.
"""

import decimal

def solve_expression(expression):
    decimal.getcontext().prec = 4  # Set precision to 4 places
    return str(decimal.Decimal(eval(expression)).quantize(decimal.Decimal('0.00')))