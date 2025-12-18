"""
QUESTION:
Write a function `InfixToPostfix(infixExpression)` that takes an infix expression as a string and returns the equivalent postfix expression as a string. The function should handle operators with varying precedence levels and parentheses. Assume the input infix expression is valid.
"""

def InfixToPostfix(infixExpression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    postfixExpression = ""

    for char in infixExpression:
        if char.isalpha():
            postfixExpression += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfixExpression += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
                postfixExpression += stack.pop()
            stack.append(char)

    while stack:
        postfixExpression += stack.pop()

    return postfixExpression