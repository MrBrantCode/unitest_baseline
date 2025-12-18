"""
QUESTION:
Create a function `calculate(x, y, z, operation)` that performs arithmetic operations based on the provided `operation` string. The function takes four arguments: three numbers (`x`, `y`, and `z`) and an `operation` string. It supports three operations: "multiply", "divide", and "subtract". If the operation is "multiply", return the product of `x`, `y`, and `z`. If the operation is "divide", return the quotient of `x` divided by `y` divided by `z`. If the operation is "subtract", return the difference of `x` minus `y` minus `z`. If the operation is not one of the specified operations, return an error message stating that the operation is not supported.
"""

def calculate(x, y, z, operation):
    if operation == "multiply":
        return x * y * z
    elif operation == "divide":
        if y == 0 or z == 0:
            return "Error: Division by zero is not allowed"
        return x / y / z
    elif operation == "subtract":
        return x - y - z
    else:
        return "Error: Operation not supported"