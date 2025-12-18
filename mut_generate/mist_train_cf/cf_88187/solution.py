"""
QUESTION:
Create a function `evaluate_expression(expression)` that evaluates a mathematical expression. The function should support the following arithmetic operators: addition (+), subtraction (-), multiplication (*), division (/), and exponentiation (^). The expression can contain multiple operators, parentheses, and nested exponentiations. The function should correctly handle operator precedence, following the standard mathematical rules, and handle negative numbers. Additionally, the function should support evaluating trigonometric functions (sin, cos, tan), logarithmic functions (log), square root function (sqrt), factorial function (fact), absolute value function (abs), natural logarithm function (ln), and power function (pow). The function should return the result of the evaluated expression as a floating-point number.
"""

import math

def evaluate_expression(expression):
    expression = expression.replace("sin", "math.sin")
    expression = expression.replace("cos", "math.cos")
    expression = expression.replace("tan", "math.tan")
    expression = expression.replace("log", "math.log")
    expression = expression.replace("sqrt", "math.sqrt")
    expression = expression.replace("fact", "math.factorial")
    expression = expression.replace("abs", "math.fabs")
    expression = expression.replace("ln", "math.log")
    expression = expression.replace("pow", "math.pow")
    expression = expression.replace("^", "**")
    result = eval(expression)
    return float(result)