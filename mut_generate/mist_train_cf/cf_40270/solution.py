"""
QUESTION:
Implement a function named `infix_to_postfix` that takes a string `expression` as input and returns the corresponding postfix expression as a string. The input expression is a properly formatted string consisting of single-digit integers and the operators `+`, `-`, `*`, and `/`, with spaces separating each element. The function should use a stack data structure to assist in the conversion process.
"""

def infix_to_postfix(expression: str) -> str:
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []

    for token in expression.split():
        if token.isdigit():
            output.append(token)
        elif token in precedence:
            while (stack and precedence.get(stack[-1], 0) >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while (stack and stack[-1] != '('):
                output.append(stack.pop())
            stack.pop()

    while stack:
        output.append(stack.pop())

    return ' '.join(output)