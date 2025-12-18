"""
QUESTION:
Implement a function `evaluate_postfix` that evaluates a postfix expression represented as a list of strings and integers, where integers represent operands and strings represent operators (+, -, *, /, ^). The function should return the result of the expression as a number. The input list is guaranteed to be a valid postfix expression.
"""

def evaluate_postfix(expression):
    stack = []
    for token in expression:
        if isinstance(token, int) or (isinstance(token, str) and token.isdigit()):
            stack.append(int(token))
        else:
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
            elif token == '^':
                stack.append(operand1 ** operand2)
    return stack.pop()