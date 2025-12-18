"""
QUESTION:
Develop a function `calculate_expression(operations, numbers)` that takes two arrays as input, `operations` and `numbers`, and returns the result of the mathematical expression formed by combining the operations and numbers in sequence. The `operations` array contains basic arithmetic tasks (+, -, *, /, %) and the `numbers` array contains integer numbers. The length of the `operations` array is one less than the length of the `numbers` array. Both arrays contain a minimum of two elements, with `operations` having at least one operation and `numbers` having at least two numbers.
"""

def calculate_expression(operations, numbers):
    # Start with the first number as string for easy combination
    expression = str(numbers[0])
    
    # Combine the operators and numbers into an expression string
    for i in range(len(operations)):
        expression += operations[i] + str(numbers[i+1])

    # Use eval to calculate the expression and return
    return eval(expression)