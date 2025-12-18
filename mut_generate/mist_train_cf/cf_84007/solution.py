"""
QUESTION:
Write a function named `do_algebra` that takes two lists as input: `operators` and `operands`. The `operators` list contains primitive arithmetic operators (+, -, *, //, **) and the `operands` list contains non-negative integers. The length of the `operators` list is always one less than the length of the `operands` list. The function should return the result of the algebraic expression constructed from the given operators and operands.
"""

def do_algebra(operators, operands):
    expression = str(operands[0])
    for i in range(len(operators)):
        expression += " " + operators[i] + " " + str(operands[i + 1])
    result = eval(expression)
    return result