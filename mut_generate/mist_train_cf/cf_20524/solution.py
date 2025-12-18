"""
QUESTION:
Evaluate the value of an expression written in reverse Polish notation, where the expression is guaranteed to be valid and result in a single integer value. The expression can contain any positive or negative integer as operands and the operators can be addition, subtraction, multiplication, and division. Implement a function named evaluate_reverse_polish_notation that takes a list of strings representing the expression as input and returns the evaluated integer value.
"""

def evaluate_reverse_polish_notation(expression):
    stack = []

    for token in expression:
        if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
            stack.append(int(token))
        elif token == '+':
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operand1 + operand2)
        elif token == '-':
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operand1 - operand2)
        elif token == '*':
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operand1 * operand2)
        elif token == '/':
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operand1 / operand2)

    return stack[0]