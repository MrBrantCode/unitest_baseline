"""
QUESTION:
Evaluate the expression using the function `evaluate_expression(expression)` where expression is a string containing the expression to be evaluated. The function should follow the order of operations (PEMDAS/BODMAS) and return the final result. The expression may include parentheses, addition, subtraction, multiplication, division, and exponentiation using the "^" symbol.
"""

def evaluate_expression(expression):
    return eval(expression.replace('^', '**'))