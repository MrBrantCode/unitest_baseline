"""
QUESTION:
Write a function `postfix_to_infix` that takes a string of postfix expression as input and returns the equivalent infix expression as a string. The function should not use any built-in functions or libraries for the conversion process. It should use a stack data structure and follow the rules for operator precedence to handle different operators correctly.
"""

def postfix_to_infix(postfix_expression):
    """
    Converts a postfix expression to an infix expression.

    Args:
        postfix_expression (str): A string of postfix expression.

    Returns:
        str: The equivalent infix expression as a string.
    """

    # Initialize an empty stack
    stack = []

    # Iterate over each character in the postfix expression
    for char in postfix_expression:
        # If the character is an operand, push it onto the stack
        if char not in '+-*/':
            stack.append(char)
        # If the character is an operator, pop the top two operands from the stack
        else:
            # Pop the top two operands from the stack
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            # Concatenate the popped operands with the operator in the infix notation
            infix_expression = f"({operand1} {char} {operand2})"
            
            # Push the resulting infix expression back onto the stack
            stack.append(infix_expression)

    # Once the entire postfix expression is processed, the stack will contain the final infix expression
    return stack[0]