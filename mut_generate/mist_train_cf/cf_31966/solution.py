"""
QUESTION:
Implement the function `evaluate_math_expression(expression)` that takes a string representing a mathematical expression as input and returns the result of the expression. The input expression can contain the four basic arithmetic operations (+, -, *, /) and parentheses to indicate the order of operations. The function should handle exceptions and return the correct result.
"""

import ast

def evaluate_math_expression(expression):
    # Using the ast module to safely evaluate the expression
    try:
        # Using the literal_eval function to evaluate the expression
        result = ast.literal_eval(expression)
        return result
    except (SyntaxError, ValueError):
        # If the expression is not a simple literal, evaluate using eval
        return eval(expression)
    except Exception as e:
        # Handle any other exceptions and return an error message
        return f"Error: {e}"