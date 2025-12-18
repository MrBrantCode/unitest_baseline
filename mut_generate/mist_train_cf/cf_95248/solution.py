"""
QUESTION:
Create a function called `evaluate_expression(expression)` that takes an arithmetic expression as input, evaluates it, and returns the result. The expression can contain addition, subtraction, multiplication, and division operations, as well as parentheses to indicate precedence. If the expression contains division by zero, the function should return "Error: Division by zero". If the input expression is invalid, the function should return "Error: Invalid expression".
"""

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except:
        return "Error: Invalid expression"