"""
QUESTION:
Create a function called `is_valid_expression` that takes a string representing a mathematical expression as input. The function should return `True` if the expression is valid and `False` otherwise. A valid expression is one that has correct usage of parentheses, brackets, and braces, as well as proper placement of operators. The expression is considered valid if it meets the following conditions:
- The parentheses, brackets, and braces are correctly nested and matched.
- The expression does not start or end with an operator.
- No two operators are adjacent to each other.
"""

def is_valid_expression(expression):
    """
    Checks if a mathematical expression is valid.

    A valid expression is one that has correct usage of parentheses, brackets, and braces, 
    as well as proper placement of operators. The expression is considered valid if it meets 
    the following conditions:
    - The parentheses, brackets, and braces are correctly nested and matched.
    - The expression does not start or end with an operator.
    - No two operators are adjacent to each other.

    Args:
        expression (str): A string representing a mathematical expression.

    Returns:
        bool: True if the expression is valid, False otherwise.
    """

    # Define the pairs of brackets
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    # Define the operators
    operators = set(['+', '-', '*', '/', '^', '%'])

    # Initialize an empty stack
    stack = []

    # Check if the expression starts or ends with an operator
    if expression[0] in operators or expression[-1] in operators:
        return False

    # Loop through each character in the string
    for i in range(len(expression)):
        char = expression[i]
        # If the character is an open bracket, push it onto the stack
        if char in bracket_pairs.values():
            stack.append(char)
        # If the character is a closing bracket
        elif char in bracket_pairs.keys():
            # If the stack is empty, return False
            if not stack:
                return False
            # Otherwise, remove the top element from the stack and compare it to the closing bracket
            else:
                top = stack.pop()
                if top != bracket_pairs[char]:
                    return False
        # If the character is an operator
        elif char in operators:
            # Check if the previous character is an operator (ignoring whitespace)
            if i > 0 and expression[i-1] in operators and expression[i-1] != ' ':
                return False

    # After checking all the characters, if the stack isn't empty, return False
    if stack:
        return False
    # Otherwise, return True
    else:
        return True