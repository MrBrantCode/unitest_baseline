"""
QUESTION:
Implement a function `evaluate_postfix(expression: str) -> int` that evaluates a postfix expression using a stack data structure. The function should take a string representing a postfix expression and return the result of the expression as an integer. The expression consists of integers and operators (+, -, *, /). The function should handle the operators and operands correctly according to the postfix notation rules, where every operator follows all of its operands. The stack should be implemented using a list in Python.
"""

def evaluate_postfix(expression: str) -> int:
    stack = []
    operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x // y}

    for token in expression.split():
        if token in operators:
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(operators[token](n1, n2))
        else:
            stack.append(int(token))
    return stack.pop()