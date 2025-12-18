"""
QUESTION:
Write a function named `evaluate_reverse_polish_notation` that takes a list of strings `expression` as input, where each string is either an integer or an operator (+, -, \*, /), and returns the result of evaluating the expression in reverse Polish notation. The expression is guaranteed to be valid and result in a single integer value.
"""

def evaluate_reverse_polish_notation(expression):
    stack = []

    for token in expression:
        if token.lstrip('-').isdigit():
            stack.append(int(token))
        elif token in ['+', '-', '*', '/']:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 / operand2)

    return stack[0]