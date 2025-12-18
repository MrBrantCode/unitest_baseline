"""
QUESTION:
Write a function `infix_to_postfix(expression)` that takes a string `expression` in infix notation and returns the equivalent expression in postfix notation. The function should handle basic arithmetic operators (+, -, *, /) and parentheses.
"""

def infix_to_postfix(expression):
    precedence = {'+':1, '-':1, '*':2, '/':2}
    stack = []
    postfix = ''
    
    for char in expression:
        if char.isalnum():
            postfix += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            if stack and stack[-1] == '(':
                stack.pop()
        else:
            while stack and stack[-1] in precedence and precedence[char] <= precedence[stack[-1]]:
                postfix += stack.pop()
            stack.append(char)
    
    while stack:
        postfix += stack.pop()
    
    return postfix