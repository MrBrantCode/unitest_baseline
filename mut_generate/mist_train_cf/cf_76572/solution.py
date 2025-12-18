"""
QUESTION:
Write a function `prefix_to_postfix(expression)` that takes a string `expression` representing a prefix mathematical expression and returns its equivalent postfix expression. The function should assume that every operator in the expression has exactly two operands and that the expression contains only alphabetic characters (representing operands) and operators.
"""

def prefix_to_postfix(expression):
    operatorStack = []
    postfix = ''

    # Read from right to left
    for operator in expression[::-1]:
        # If operator, push to stack
        if operator.isalpha():
            operatorStack.append(operator)
        else:
            # Pop two elements
            operand1 = operatorStack.pop()
            operand2 = operatorStack.pop()

            # Create new expression and push back
            new_expr = operand1 + operand2 + operator
            operatorStack.append(new_expr)

    postfix = operatorStack[0]
    return postfix