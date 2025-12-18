"""
QUESTION:
Create a function `perform_math_operations` that takes two lists, `operators_list` and `operands_list`, as input. The function should formulate and evaluate a mathematical expression based on the input lists. `operators_list` contains the operators (+, -, *, //, **) and `operands_list` contains non-negative integers. The count of `operators_list` is one less than the count of `operands_list`. The function should follow the order of operations according to the BODMAS rule and return the result of the evaluated expression.
"""

def perform_math_operations(operators_list, operands_list):
    expression = str(operands_list[0])
    for i in range(1, len(operands_list)):
        expression += operators_list[i-1] + str(operands_list[i])
    return eval(expression)