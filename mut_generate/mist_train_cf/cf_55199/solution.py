"""
QUESTION:
Create a function named `calculate` that evaluates a string `expr` representing an algebraic equation in infix notation using the Shunting-Yard algorithm with a Last In, First Out (LIFO) stack data structure. The function should handle operators with different precedence levels, including parentheses for grouping, and return the final result of the equation. The input string may contain numeric operands, operators (+, -, *, /, ^), and parentheses.
"""

def calculate(expr):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

    def apply_operation(op, a, b):
        if op == '+': return a + b
        elif op == '-': return a - b
        elif op == '*': return a * b
        elif op == '/': return a / b
        elif op == '^': return a ** b

    def greater_precedence(op1, op2):
        return precedence[op1] > precedence[op2]

    operator_stack = []
    operand_stack = []
    tokens = expr.replace("(", " ( ").replace(")", " ) ").split()

    for token in tokens:
        if token.isnumeric():
            operand_stack.append(int(token))
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack[-1] != '(':
                op = operator_stack.pop()
                right = operand_stack.pop()
                left = operand_stack.pop()
                result = apply_operation(op, left, right)
                operand_stack.append(result)
            operator_stack.pop()  # Remove the '('
        else:
            while (operator_stack and operator_stack[-1] in precedence 
                   and greater_precedence(operator_stack[-1], token)):
                op = operator_stack.pop()
                right = operand_stack.pop()
                left = operand_stack.pop()
                result = apply_operation(op, left, right)
                operand_stack.append(result)
            operator_stack.append(token)

    while operator_stack:
        op = operator_stack.pop()
        right = operand_stack.pop()
        left = operand_stack.pop()
        result = apply_operation(op, left, right)
        operand_stack.append(result)

    return operand_stack[0]