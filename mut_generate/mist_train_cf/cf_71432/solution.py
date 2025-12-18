"""
QUESTION:
Write a function named `execute_arithmetic_functions` that takes two lists as input: `operation_elements` and `number_elements`. The `operation_elements` list contains basic arithmetic operations (+, -, *, //, **), and the `number_elements` list contains non-negative integers. The function should construct and evaluate a mathematical expression by sequentially applying the operations to the numbers. The length of `operation_elements` is one less than the length of `number_elements`, and both lists have at least two elements. Return the result of the evaluated expression.
"""

def execute_arithmetic_functions(operation_elements, number_elements):
    final_result = str(number_elements[0]) 
    for i in range(len(operation_elements)):
        final_result += " " + operation_elements[i] + " " + str(number_elements[i + 1])
    final_result = eval(final_result) 
    return final_result