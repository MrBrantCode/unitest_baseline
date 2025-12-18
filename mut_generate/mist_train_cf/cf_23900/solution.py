"""
QUESTION:
Write a function `postfix_to_infix(expression)` that takes a string `expression` representing an expression in postfix notation and returns the equivalent expression in infix notation. The function should follow the rule that when an operator is encountered, it should be placed between the two most recently added operands. The input expression is a space-separated string of operands and operators, where operands are numbers or letters and operators are one of +, -, *, /.
"""

def postfix_to_infix(expression):
    stack = []
    tokens = expression.split()
    operators = set(['+', '-', '*', '/'])

    for token in tokens:
        if token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(f"({operand1} {token} {operand2})")
        else:
            stack.append(token)

    return stack[0]