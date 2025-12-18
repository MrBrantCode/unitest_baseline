"""
QUESTION:
Write a function `postfix_to_infix(expression)` that converts a given postfix expression to infix notation. The function should handle the four basic arithmetic operations (+, -, *, /) and parentheses. The input expression is guaranteed to contain only valid operators and operands. The function should return a string representing the expression in infix notation.
"""

def postfix_to_infix(expression):
    stack = []
    
    for char in expression:
        if char.isdigit():
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append("(" + operand1 + char + operand2 + ")")
    
    return stack[0]