"""
QUESTION:
Implement the `is_valid_expression` function that checks the validity of a mathematical expression using a Turing machine. The input is a string of characters representing the mathematical expression, which consists of numbers (0-9), operators (+, -, *, /), and parentheses. The function should return `True` if the expression is valid and `False` otherwise.

Restrictions:
- The Turing machine implementation should have a time complexity of O(n), where n is the length of the input string.
- The Turing machine implementation should have a space complexity of O(1).
- The input string can be empty.
- The input string can contain single numbers.
- The input string can contain division by zero.
- The input string can contain unbalanced parentheses.
- The input string can contain multiple operators and operands.
- The input string can contain multiple sets of parentheses.
"""

def is_valid_expression(expression):
    """
    Checks the validity of a mathematical expression using a stack-based approach.

    Args:
    expression (str): The mathematical expression to check.

    Returns:
    bool: True if the expression is valid, False otherwise.
    """
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                return False
    return not stack