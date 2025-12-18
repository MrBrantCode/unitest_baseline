"""
QUESTION:
Create a function named `perform_operation` that takes three parameters: two n-digit integers `num1` and `num2`, and a string `operation` representing one of the four basic arithmetic operations (+, -, *, /). The function should return the result of the operation. If the operation is subtraction, it should return the difference. If the operation is division and the second number is zero, or if the operation is invalid, the function should return an error message.
"""

def perform_operation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Error! Invalid operation."