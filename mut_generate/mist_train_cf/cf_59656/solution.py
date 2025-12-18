"""
QUESTION:
Implement a function named `validate_expression` that takes a string `expression` as input and returns `True` if the expression is a valid logical statement and `False` otherwise. The expression may contain logical operators (`AND`, `OR`, `NOT`, `IF-THEN`, `IFF`), logical constants (`true`, `false`), and parentheses. The function should check for correct usage of parentheses and ensure that only valid operators, operands, and parentheses are used. The input expression may be in infix, prefix, or postfix notation.
"""

def validate_expression(expression):
    """
    Validates a logical expression containing operators, operands, and parentheses.

    Args:
    expression (str): The logical expression to be validated.

    Returns:
    bool: True if the expression is valid, False otherwise.
    """
    valid_operators = ['AND', 'OR', 'NOT', 'IF-THEN', 'IFF']
    valid_terms = ['true', 'false']
    stack = []

    # Check for parentheses
    for character in expression:
        if character == '(':
            stack.append(character)
        elif character == ')':
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        return False

    words = expression.split()

    for word in words:
        if word in valid_operators or word in valid_terms or word in ['(', ')']:
            continue
        else:
            return False

    return True