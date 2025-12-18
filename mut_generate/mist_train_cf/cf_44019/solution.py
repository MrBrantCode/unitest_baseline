"""
QUESTION:
Write a function named `prefix_to_postfix` that takes a string of prefix notation as input and returns the equivalent string in postfix notation. The input string will only contain uppercase letters (representing operands) and the operators '+', '-', '*', '/'. The function should not use any external libraries.
"""

from collections import deque

def prefix_to_postfix(prefix):
    """Convert prefix to postfix."""
    # Create a stack
    stack = deque()

    # Reverse prefix
    rev = prefix[::-1]

    for char in rev:
        if char in ["+", "-", "*", "/"]:
            # Pop two operands from stack
            operand1 = stack.pop()
            operand2 = stack.pop()
            # Create string with operands and operator
            new_string = operand1 + operand2 + char
            # Push back into the stack
            stack.append(new_string)
        else:
            # If operand, push into stack
            stack.append(char)
    
    # The final string in the stack is the postfix notation
    return stack.pop()