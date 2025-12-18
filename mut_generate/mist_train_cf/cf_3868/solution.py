"""
QUESTION:
Create a function called `evaluate_expression(expression)` to evaluate a mathematical expression. The function should support the following arithmetic operators: addition (+), subtraction (-), multiplication (*), division (/), and exponentiation (^). It should correctly handle operator precedence, following standard mathematical rules, and return the result of the evaluated expression as a floating-point number. The expression can contain multiple operators, parentheses, nested exponentiations, negative numbers, and the following functions: sin(x), cos(x), tan(x), log(x), sqrt(x), fact(x), abs(x), ln(x), and pow(x, y).
"""

import math

def evaluate_expression(expression):
    # Replace trigonometric functions with their math module equivalents
    expression = expression.replace("sin", "math.sin")
    expression = expression.replace("cos", "math.cos")
    expression = expression.replace("tan", "math.tan")
    
    # Replace logarithmic functions with their math module equivalents
    expression = expression.replace("log", "math.log")
    
    # Replace square root function with math module equivalent
    expression = expression.replace("sqrt", "math.sqrt")
    
    # Replace factorial function with math module equivalent
    expression = expression.replace("fact", "math.factorial")
    
    # Replace absolute value function with math module equivalent
    expression = expression.replace("abs", "math.fabs")
    
    # Replace natural logarithm function with math module equivalent
    expression = expression.replace("ln", "math.log")
    
    # Replace power function with math module equivalent
    expression = expression.replace("pow", "math.pow")
    
    # Replace '^' with '**'
    expression = expression.replace("^", "**")
    
    # Evaluate the expression and return the result as a float
    result = eval(expression)
    return float(result)