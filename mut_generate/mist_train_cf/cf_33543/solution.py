"""
QUESTION:
Evaluate the result of a mathematical expression in postfix notation. 

Create a function `evaluate_postfix(expression)` that takes a string `expression` as input, representing a mathematical expression in postfix notation. The input string will consist of numbers and operators (+, -, *, /) separated by spaces. Assume that the input is always valid and that the expression will always result in a finite answer. The function should return the result of the evaluated expression.
"""

def evaluate_postfix(expression):
    stack = []
    operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}

    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operators[token](operand1, operand2)
            stack.append(result)

    return stack.pop()