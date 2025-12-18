"""
QUESTION:
Implement a function `evaluate_expression(expression)` that takes a string of an arithmetic expression containing addition, subtraction, multiplication, and division operations, and returns the result of the expression as a number. The function should handle error cases by returning "Error: Division by zero" if division by zero occurs and "Error: Invalid expression" for any other invalid input. The expression can contain parentheses to indicate precedence, and the function should follow the correct order of operations.
"""

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except:
        return "Error: Invalid expression"