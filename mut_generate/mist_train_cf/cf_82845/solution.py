"""
QUESTION:
Write a function `evaluate_postfix(expression)` that evaluates a postfix expression given as a string. The expression contains single-digit integers and four basic arithmetic operators (+, -, *, /). The function should return the evaluated value of the expression. Assume that the input postfix expression is always valid, i.e., there are always two valid operands before an operator, and division by zero will not occur. The function should also assume integer division for the division operation.
"""

def evaluate_postfix(expression):
    """
    Function to evaluate a postfix expression.
    """
    # Create an empty stack
    stack = []

    for i in expression.split():
        # If the element is an operator, pop two operands from the stack
        # perform the operation, and push the result back to the stack
        if i in ['+', '-', '*', '/']:
            op2 = stack.pop()
            op1 = stack.pop()

            if i == '+':
                result = op1 + op2
            elif i == '-':
                result = op1 - op2
            elif i == '*':
                result = op1 * op2
            else:
                result = op1 / op2

            stack.append(result)
        # If the element is an operand, push it to the stack
        else:
            stack.append(int(i))

    # The final result is the only element left in the stack
    return stack[0]