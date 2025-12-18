"""
QUESTION:
Create a function called `calculate` that evaluates a given mathematical expression and returns the result. The expression can contain basic arithmetic operations, exponentiation, trigonometric functions (sin, cos, tan), and parentheses. The input expression should use '^' for exponentiation and may not contain 'math.' prefix for trigonometric functions. The function should handle the expression as a string and return the calculated result as a number.
"""

import math

def calculate(expression):
    expression = expression.replace('^', '**')
    expression = expression.replace('sin', 'math.sin')
    expression = expression.replace('cos', 'math.cos')
    expression = expression.replace('tan', 'math.tan')
    expression = expression.replace('sqrt', 'math.sqrt')
    
    result = eval(expression)
    return result