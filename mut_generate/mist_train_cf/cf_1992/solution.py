"""
QUESTION:
Convert the function name to postfix_to_infix and create a function that takes a string expression as input, representing an expression in postfix notation. The function should convert this expression to infix notation and return it as a string. The input expression will contain only valid arithmetic operations (+, -, *, /, %), parentheses, and operands. Do not use any built-in libraries or functions that directly solve this problem.
"""

def postfix_to_infix(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            new_expression = '(' + operand1 + char + operand2 + ')'
            stack.append(new_expression)
    return stack.pop()