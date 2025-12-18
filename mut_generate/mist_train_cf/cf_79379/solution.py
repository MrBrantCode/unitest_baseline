"""
QUESTION:
Write a function named `do_algebra` that takes two parameters, `operator` and `operand`. The `operator` parameter is a list of basic arithmetic operations (+, -, *, //, **) and the `operand` parameter is a list of non-negative integers. The `operator` list's length must be one less than the `operand` list's length. The function should construct and evaluate an algebraic expression using the provided operators and operands, and return the result.
"""

def do_algebra(operator, operand):
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
    return result