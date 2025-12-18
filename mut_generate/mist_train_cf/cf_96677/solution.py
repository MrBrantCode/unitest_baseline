"""
QUESTION:
Implement a function `evaluate_expression(expression)` that evaluates a mathematical expression represented as a string and returns the result as a floating-point number. The expression can contain addition (+), subtraction (-), multiplication (*), division (/), and exponentiation (^) operators, as well as parentheses to indicate the order of operations. The operands can be integers or floating-point numbers. Do not use built-in functions or libraries for evaluating mathematical expressions. The time complexity of the algorithm should be O(n), where n is the length of the expression string.
"""

def evaluate_expression(expression):
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    def apply_operation(operands, operators):
        operand2 = operands.pop()
        operand1 = operands.pop()
        operator = operators.pop()
        if operator == '+':
            result = operand1 + operand2
        elif operator == '-':
            result = operand1 - operand2
        elif operator == '*':
            result = operand1 * operand2
        elif operator == '/':
            result = operand1 / operand2
        elif operator == '^':
            result = operand1 ** operand2
        operands.append(result)

    operands = []
    operators = []

    operand = ''
    for char in expression:
        if char.isdigit() or char == '.':
            operand += char
        else:
            if operand:
                operands.append(float(operand))
                operand = ''
            if char == '(':
                operators.append(char)
            elif char == ')':
                while operators and operators[-1] != '(':
                    apply_operation(operands, operators)
                operators.pop()
            elif char in precedence:
                while operators and precedence[char] <= precedence.get(operators[-1], 0):
                    apply_operation(operands, operators)
                operators.append(char)

    if operand:
        operands.append(float(operand))

    while operators:
        apply_operation(operands, operators)

    return operands[-1]