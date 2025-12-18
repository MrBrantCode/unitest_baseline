"""
QUESTION:
Write a function `convert_to_postfix` that takes an infix expression with parentheses and operators (+, -, *, /) as input, and returns the corresponding postfix expression. The function should handle the order of operations based on the precedence of the operators, where '*' and '/' have higher precedence than '+' and '-'.
"""

def convert_to_postfix(infix_expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    postfix_expression = ""

    for char in infix_expression:
        if char.isalpha():
            postfix_expression += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix_expression += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] in precedence and precedence[stack[-1]] >= precedence[char]:
                postfix_expression += stack.pop()
            stack.append(char)

    while stack:
        postfix_expression += stack.pop()

    return postfix_expression