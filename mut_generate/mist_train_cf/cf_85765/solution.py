"""
QUESTION:
Write a function `compute_arithmetic_seq` that takes two lists, `operator_set` and `operand_set`, as input. The function should apply the operations in `operator_set` on the operands in `operand_set` in order and return the result. `operator_set` contains at least one operator and `operand_set` contains at least two positive integers. The length of `operator_set` is one less than the length of `operand_set`. The operators in `operator_set` can be '+', '-', '*', '//', or '**'.
"""

import operator

def compute_arithmetic_seq(operator_set, operand_set):
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "//": operator.floordiv,
        "**": operator.pow
    }

    result = operand_set[0]

    for index in range(len(operator_set)):
        result = ops[operator_set[index]](result, operand_set[index + 1])

    return result