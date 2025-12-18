"""
QUESTION:
Create a function called `calculate()` that takes in three arguments: two numbers `x` and `y`, and a string `operation`. The function should perform the operation specified by the string on `x` and `y`. If the `operation` is "multiply", return the product of `x` and `y`. If the `operation` is "divide", return the quotient of `x` and `y`. If the `operation` is neither "multiply" nor "divide", return an error message stating that the operation is not supported. Assume the multiply and divide operations are defined elsewhere.
"""

def calculate(x, y, operation):
    if operation == "multiply":
        return x * y
    elif operation == "divide":
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero"
    else:
        return "Error: Operation not supported"