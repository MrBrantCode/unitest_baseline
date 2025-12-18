"""
QUESTION:
Write a function `postfix_to_infix(expression)` that converts a given postfix expression into an infix expression. The input `expression` is a string of space-separated numbers and operators (+, -, *, /). The function should return the equivalent infix expression as a string. The output should have the correct operator precedence and be enclosed in parentheses where necessary.
"""

def postfix_to_infix(expression):
    stack = []
    for c in expression.split():
        if c in "+-*/":
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append("({} {} {})".format(operand2, c, operand1))
        else:
            stack.append(c)
    return stack[0]