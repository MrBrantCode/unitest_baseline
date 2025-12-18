"""
QUESTION:
Write a function `infix_to_postfix(expression: str) -> str` to convert an infix expression to a postfix expression. The infix expression can include operators "+", "-", "*", "/", "%", parentheses, variables (single letters), and constants (positive integers). The function should preserve parentheses, place operators after their operands, maintain the order of evaluation, and handle operators of the same precedence from left to right. Assume the input expression is valid, well-formed, and does not contain whitespace characters, and its length does not exceed 10^5 characters.
"""

def infix_to_postfix(expression: str) -> str:
    """
    Converts an infix expression to a postfix expression.

    Args:
    expression (str): The infix expression to convert.

    Returns:
    str: The postfix expression equivalent to the input infix expression.
    """
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}

    stack = []
    postfix = ""

    for char in expression:
        # If the character is an operand (variable or constant), append it to the postfix expression.
        if char.isalpha() or char.isdigit():
            postfix += char

        # If the character is an opening parenthesis, push it onto the stack.
        elif char == '(':
            stack.append(char)

        # If the character is a closing parenthesis, pop operators from the stack and append them to the postfix expression until an opening parenthesis is encountered.
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            # Discard the opening parenthesis.
            stack.pop()

        # If the character is an operator, pop operators from the stack and append them to the postfix expression until an operator of lower precedence (or an opening parenthesis) is encountered.
        elif char in precedence:
            while stack and stack[-1] in precedence and precedence[stack[-1]] >= precedence[char]:
                postfix += stack.pop()
            # Push the current operator onto the stack.
            stack.append(char)

    # Pop any remaining operators from the stack and append them to the postfix expression.
    while stack:
        postfix += stack.pop()

    return postfix