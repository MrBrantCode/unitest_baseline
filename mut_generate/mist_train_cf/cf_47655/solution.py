"""
QUESTION:
Write a function `categorize_expression` that takes a string representing an arithmetic expression as input and returns the mathematical nature of the expression. The function should categorize the expression based on the operations it contains, such as addition, subtraction, multiplication, and division, and consider the order of operations (BIDMAS or PEMDAS).
"""

def categorize_expression(expression):
    """
    Categorize the mathematical nature of an arithmetic expression.

    Args:
    expression (str): A string representing an arithmetic expression.

    Returns:
    str: A string describing the mathematical nature of the expression.
    """

    # Initialize flags to track the operations in the expression
    has_addition = False
    has_subtraction = False
    has_multiplication = False
    has_division = False

    # Iterate over each character in the expression
    for char in expression:
        # Check for addition
        if char == '+':
            has_addition = True
        # Check for subtraction
        elif char == '-':
            has_subtraction = True
        # Check for multiplication
        elif char == '*':
            has_multiplication = True
        # Check for division
        elif char == '/':
            has_division = True

    # Categorize the expression based on the operations it contains
    if has_addition and has_multiplication:
        return "combination of addition and multiplication"
    elif has_addition and has_subtraction:
        return "combination of addition and subtraction"
    elif has_multiplication and has_division:
        return "combination of multiplication and division"
    elif has_addition:
        return "addition"
    elif has_subtraction:
        return "subtraction"
    elif has_multiplication:
        return "multiplication"
    elif has_division:
        return "division"
    else:
        return "unknown"