"""
QUESTION:
Create a function `calculate_expression` that takes two lists as input, `operations` and `numbers`, and returns the result of the mathematical expression formed by combining the numbers with the operations. The `operations` list contains elementary arithmetic operations (+, -, *, /, %) and the `numbers` list contains integers. The length of the `operations` list is one less than the length of the `numbers` list, and each list contains at least two elements.
"""

def calculate_expression(operations, numbers):
    expression = str(numbers[0])
    for i in range(1, len(numbers)):
        expression += ' ' + operations[i-1] + ' ' + str(numbers[i])
    return eval(expression)