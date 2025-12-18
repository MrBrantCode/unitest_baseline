"""
QUESTION:
Write a function `infix_to_postfix(expression)` that converts an infix expression to a postfix expression. The infix expression may contain variables (single letters), constants (positive integers), the operators "+", "-", "*", "/", "%", and parentheses. The function should maintain the order of evaluation, preserve parentheses, place operators after their operands, and handle operators with the same precedence from left to right. Assume the input expression is valid and well-formed, with no whitespace characters, and possibly containing duplicate variables.
"""

def infix_to_postfix(expression):
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}
    stack = []
    postfix = ''
    
    for char in expression:
        if char.isalpha() or char.isdigit():
            postfix += char
        elif char in operators:
            while stack and stack[-1] in operators and operators[char] <= operators[stack[-1]]:
                postfix += stack.pop()
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
    
    while stack:
        postfix += stack.pop()
    
    return postfix