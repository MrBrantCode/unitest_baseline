"""
QUESTION:
Create a function named `operate_on_two_numbers` that takes three parameters: two numbers `a` and `b`, and a string `operation`. The function should perform the operation specified by the string on the two numbers. The operation string can be one of the following: "add", "subtract", "multiply", "divide". If the operation string is "divide" and `b` is zero, the function should return an error message "Error: Division by zero is not allowed!". If the operation string does not match any of the specified operations, the function should return an error message "Error: Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide' as operation.". The function should return the result of the operation otherwise.
"""

def operate_on_two_numbers(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Division by zero is not allowed!"
        return a / b
    else:
        return "Error: Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide' as operation."