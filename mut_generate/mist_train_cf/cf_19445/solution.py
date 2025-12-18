"""
QUESTION:
Write a function named `evaluate_expression` that takes a string `expression` as input and returns a decimal number as output. The expression may include parentheses and the following operators: +, -, *, /. The expression may also contain decimal numbers.
"""

import decimal

def evaluate_expression(expression):
    operands = []
    operators = []
    num = ""
    
    for ch in expression:
        if ch.isdigit() or ch == '.':
            num += ch
        elif ch == ' ':
            continue
        elif ch in ['+', '-', '*', '/']:
            if num:
                operands.append(decimal.Decimal(num))
                num = ""
            operators.append(ch)
        elif ch == '(':
            operators.append(ch)
        elif ch == ')':
            if num:
                operands.append(decimal.Decimal(num))
                num = ""
            while operators[-1] != '(':
                operator = operators.pop()
                operand2 = operands.pop()
                operand1 = operands.pop()
                result = evaluate_operation(operand1, operand2, operator)
                operands.append(result)
            operators.pop()  # Pop the opening parenthesis
    if num:
        operands.append(decimal.Decimal(num))
        
    while operators:
        operator = operators.pop()
        operand2 = operands.pop()
        operand1 = operands.pop()
        result = evaluate_operation(operand1, operand2, operator)
        operands.append(result)
    
    return float(operands[0])


def evaluate_operation(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2