"""
QUESTION:
Write a function `calculate_expression` that takes two lists as input: `operations` and `numbers`. The `operations` list contains basic arithmetic operators (+, -, *, /, %) and the `numbers` list contains integers. The function should construct and evaluate a mathematical expression using the given operators and numbers. 

The function should satisfy the following conditions:
- The length of the `operations` list is one less than the length of the `numbers` list.
- The `numbers` list can contain both positive and negative integers.
- The `operations` list must have at least one operation, and the `numbers` list must have at least two numbers.

The function should return the result of the evaluated expression or an error message if the input is invalid.
"""

def calculate_expression(operations, numbers):
    # Check if the length of the operations list is one less than length of the numbers list
    if len(operations) != len(numbers) - 1:
        return "Error: Invalid input."
    # Check if the numbers list has at least two numbers
    if len(numbers) < 2:
        return "Error: Not enough numbers."
    # Check if the operations list has at least one operation
    if len(operations) < 1:
        return "Error: Not enough operations."
    
    # Form the expression to be calculated
    expression = str(numbers[0])
    for i in range(len(operations)):
        expression += operations[i] + str(numbers[i+1])
    
    # Evaluate the expression
    return eval(expression)