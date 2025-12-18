"""
QUESTION:
Implement a function named `do_algebra` that takes two lists, `operators` and `operands`, as input. The `operators` list contains basic arithmetic operations (+, -, *, //, **) and the `operands` list contains non-negative integers. The length of the `operators` list is one less than the length of the `operands` list. The function should apply the operators to the corresponding operands from left to right and return the final result. The `operators` list has at least one operator and the `operands` list has at least two operands.
"""

def do_algebra(operators, operands):
    """
    Applies arithmetic operations to corresponding operands from left to right.

    Args:
        operators (list): A list of basic arithmetic operations (+, -, *, //, **).
        operands (list): A list of non-negative integers.

    Returns:
        The final result of applying the operators to the operands.
    """
    result = operands[0]
    for i in range(len(operators)):
        op = operators[i]
        if op == '+':
            result += operands[i+1]
        elif op == '-':
            result -= operands[i+1]
        elif op == '*':
            result *= operands[i+1]
        elif op == '//':
            result //= operands[i+1]
        elif op == '**':
            result **= operands[i+1]
    return result