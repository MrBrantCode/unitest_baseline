"""
QUESTION:
Implement a function named `convert_to_postfix` that takes an expression in infix notation as input and returns its equivalent in postfix notation. The function should handle expressions containing letters (A-Z) and basic arithmetic operators (+, -, *, /).
"""

def convert_to_postfix(expression):
    """
    Converts an infix expression to postfix notation.

    Args:
    expression (str): The infix expression to be converted.

    Returns:
    str: The postfix equivalent of the input expression.
    """
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = ''
    operator_stack = []

    for char in expression:
        if char.isalpha():
            output += char
        elif char in precedence:
            while (operator_stack and 
                   operator_stack[-1] in precedence and 
                   precedence[operator_stack[-1]] >= precedence[char]):
                output += operator_stack.pop()
            operator_stack.append(char)
        elif char == '(':
            operator_stack.append(char)
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                output += operator_stack.pop()
            if operator_stack and operator_stack[-1] == '(':
                operator_stack.pop()

    while operator_stack:
        output += operator_stack.pop()

    return output