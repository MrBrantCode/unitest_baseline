"""
QUESTION:
Create a function called `calculate(num1, num2, operation)` that takes two numbers `num1` and `num2` and an arithmetic operation `operation` as input. The function should apply the specified operation on the two numbers and return the result along with the operation performed. The operation can be one of the following: addition, subtraction, multiplication, or division. If the operation is division and the second number is zero, the function should return an error message "Error: Division by zero is not allowed." If the operation is not one of the four arithmetic operations, the function should return an error message "Error: Invalid operation."
"""

def calculate(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
        operator = 'addition'
    elif operation == '-':
        result = num1 - num2
        operator = 'subtraction'
    elif operation == '*':
        result = num1 * num2
        operator = 'multiplication'
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            result = num1 / num2
            operator = 'division'
    else:
        return "Error: Invalid operation."

    return f"The result of {operator} between {num1} and {num2} is: {result}"