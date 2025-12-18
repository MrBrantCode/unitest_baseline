"""
QUESTION:
Evaluate a reverse Polish notation (RPN) expression represented as a list of strings. The function `evaluateRPN` takes a list of strings as input where each string is either an operator ("+", "-", "*", "/") or an operand (an integer represented as a string). The function should return the result of the RPN expression. The division should truncate toward zero.
"""

def evaluateRPN(tokens):
    stack = []
    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[0]