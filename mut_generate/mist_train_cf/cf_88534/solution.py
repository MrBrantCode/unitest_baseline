"""
QUESTION:
Write a function `evaluate_expression(expression, modulo)` that classifies the type of the expression when it is evaluated modulo a given integer. The expression is a string containing integers and the operators +, -, *, /, and %, and each integer and operator is separated by a space. The function should return "Integer" if the evaluated expression is an integer, "Float" if it is a floating-point number, and "Undefined" if it is undefined (e.g., division by zero). The arithmetic expression follows the usual precedence rules, and the modulo operation should be performed after evaluating the expression.
"""

def evaluate_expression(expression, modulo):
    stack = []

    for element in expression.split():
        if element.isdigit():
            stack.append(int(element))
        elif element == '/':
            divisor = stack.pop()
            if divisor == 0:
                return "Undefined"
            dividend = stack.pop()
            stack.append(dividend / divisor)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if element == '+':
                stack.append(operand1 + operand2)
            elif element == '-':
                stack.append(operand1 - operand2)
            elif element == '*':
                stack.append(operand1 * operand2)
            elif element == '%':
                stack.append(operand1 % operand2)

    if len(stack) == 1:
        result = stack[0] % modulo
        if isinstance(result, int):
            return "Integer"
        elif isinstance(result, float):
            return "Float"
    return "Undefined"