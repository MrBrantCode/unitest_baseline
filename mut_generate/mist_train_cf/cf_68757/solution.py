"""
QUESTION:
Create a function `calculate_expression(operations, numbers)` that takes two lists as input: `operations` and `numbers`. The `operations` list contains basic arithmetic operations (+, -, *, /, %) and the `numbers` list contains integers. The function should create and evaluate a mathematical expression using the given operations and numbers. The length of the `operations` list is one less than the length of the `numbers` list, and both lists have a minimum length of 1 and 2, respectively. The function should return the result of the evaluated expression.
"""

def calculate_expression(operations, numbers):
    expression = str(numbers[0])
    for i in range(len(operations)):
        expression += " " + operations[i] + " " + str(numbers[i+1])
    return eval(expression)