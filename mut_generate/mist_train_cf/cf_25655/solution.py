"""
QUESTION:
Write a function `evaluate_expression(expression)` that evaluates a given mathematical expression. The input expression is a string containing valid mathematical operators (+, -, *, /) and numbers. The function should return the result of the expression as a number.
"""

def evaluate_expression(expression):
    '''Returns the evaluation of a given mathematical expression.'''
    return eval(expression)