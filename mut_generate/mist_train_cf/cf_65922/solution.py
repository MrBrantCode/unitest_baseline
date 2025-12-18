"""
QUESTION:
Write a function `calculate` that takes a string representing a mathematical expression as input and returns the result of the expression. The expression may include addition, subtraction, multiplication, division, parentheses, negative numbers, and decimal points. If the expression involves division by zero, the function should return an error message "Error: Division by zero is undefined." and catch any other exceptions with a corresponding error message.
"""

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is undefined."
    except Exception as e:
        return f"Error: {str(e)}"