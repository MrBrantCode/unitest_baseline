"""
QUESTION:
Evaluate the value of a given postfix expression using a stack, assuming the expression contains only single-digit numbers and basic arithmetic operators (+, -, *, /). The function should take a string representing the postfix expression as input and return the result of the evaluation as an integer.
"""

def evaluate_postfix(expression):
    """
    Evaluate the value of a given postfix expression using a stack.

    Args:
    expression (str): A string representing the postfix expression.

    Returns:
    int: The result of the evaluation as an integer.
    """
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            if char == '+':
                stack.append(op2 + op1)
            elif char == '-':
                stack.append(op2 - op1)
            elif char == '*':
                stack.append(op2 * op1)
            elif char == '/':
                stack.append(op2 // op1) # Use integer division
    return stack[0]