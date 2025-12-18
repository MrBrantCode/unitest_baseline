"""
QUESTION:
Create a function `evaluate_expression` that takes two parameters: a string representing an arithmetic expression and an integer representing the modulo value. The function should evaluate the expression according to the usual precedence rules, perform the modulo operation, and return the type of the result as "Integer", "Float", or "Undefined" in case of division by zero.
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
        result = stack[0]
        if isinstance(result, int):
            result = result % modulo
            return "Integer"
        elif isinstance(result, float):
            return "Float"
    return "Undefined"