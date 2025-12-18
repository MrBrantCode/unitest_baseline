"""
QUESTION:
Create a function called `evaluate_expression` that takes a string `exp` representing a mathematical expression in infix notation, where the expression may include square roots (denoted as "root()") and exponentiation (denoted as "**"). The function should return the calculated result as a number. If the input expression is invalid or an error occurs during calculation, the function should return an error message.
"""

import math

def evaluate_expression(exp):
    try:
        # Replace 'root' with 'math.sqrt' in the expression
        exp = exp.replace("root", "math.sqrt")

        # Evaluate and return the result
        return eval(exp)

    except SyntaxError:
        return "Error: Incorrect syntax in the mathematical expression."
    except:
        return "Error: An unexpected error occurred during calculation."