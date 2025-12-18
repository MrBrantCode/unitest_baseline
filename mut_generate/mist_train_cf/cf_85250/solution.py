"""
QUESTION:
Implement a function `calculate_expression` that evaluates a complex mathematical expression given as a string. The function should handle addition (+), subtraction (-), multiplication (*), division (/), and parentheses for indicating order of operations, following the usual rules of arithmetic. The input string will contain only valid characters and the function should return the result of the evaluated expression.
"""

def calculate_expression(expression):
    try:
        return eval(expression)
    except:
        return 'Invalid expression'