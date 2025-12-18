"""
QUESTION:
Write a function `postfix_to_infix(expression)` that converts a postfix expression into infix notation. The function should handle arithmetic operations (+, -, *, /) and parentheses. The input expression is guaranteed to be valid and contain only operators and operands. The function should return a string representing the expression in infix notation.
"""

def postfix_to_infix(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])
    
    for char in expression:
        if char not in operators:
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append('({}{}{})'.format(operand1, char, operand2))
    
    return stack.pop()