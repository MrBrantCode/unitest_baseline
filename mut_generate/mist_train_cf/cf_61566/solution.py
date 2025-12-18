"""
QUESTION:
Write a function `perform_math_operations` that takes two lists as input: `operators_list` and `operands_list`. The `operators_list` contains elementary arithmetic operations (+, -, *, //, **) and `operands_list` contains non-negative integers. The length of `operators_list` is one less than the length of `operands_list`. The function should apply the operations in the order they appear in the lists, using the operands in the same order, and return the final result.
"""

def perform_math_operations(operators_list, operands_list):
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '//': lambda a, b: a // b,
        '**': lambda a, b: a ** b
    }

    result = operands_list[0]
    for operator, operand in zip(operators_list, operands_list[1:]):
        result = ops[operator](result, operand)

    return result