"""
QUESTION:
Write a function named `evaluate` that evaluates an expression written in reverse Polish notation. The input will be a list of strings where each string is either an operator ('+', '-', '*', '/') or a positive integer. The function should return the result of the evaluated expression as an integer.
"""

def evaluate(expression):
    stack = []
    for element in expression:
        if element.isdigit():
            stack.append(int(element))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if element == '+':
                stack.append(operand1 + operand2)
            elif element == '-':
                stack.append(operand1 - operand2)
            elif element == '*':
                stack.append(operand1 * operand2)
            elif element == '/':
                stack.append(operand1 // operand2)
    return stack.pop()