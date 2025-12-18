"""
QUESTION:
Convert the given infix mathematical expression to postfix notation. The function should take a string representing a valid infix mathematical expression as input and return the equivalent postfix expression as a string. The expression may contain single-letter variable names, the four basic arithmetic operators (+, -, *, /), and parentheses to denote operator precedence. Assume the input is always a valid infix expression.
"""

def infix_to_postfix(infix_expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    postfix = ''

    for char in infix_expression:
        if char.isalpha():
            postfix += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            if stack and stack[-1] == '(':
                stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
                postfix += stack.pop()
            stack.append(char)

    while stack:
        postfix += stack.pop()

    return postfix