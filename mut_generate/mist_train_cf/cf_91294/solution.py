"""
QUESTION:
Write a function called `postfix_to_infix` that takes a string `expression` representing a valid postfix notation expression containing digits and arithmetic operators (+, -, *, /) as input, and returns a string representing the equivalent infix notation expression. The function should handle parentheses and not use any built-in libraries or functions that directly solve this problem.
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