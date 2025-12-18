"""
QUESTION:
Write a function called `calculator` that takes two integers `a` and `b`, and a string `operation` as input, and returns the result of the specified operation on `a` and `b`. The `operation` can be 'add', 'subtract', 'multiply', or 'divide'. The function should handle non-integer inputs, division by zero, and unsupported operations, and return an error message in these cases.
"""

def calculator(a, b, operation):
    # Checking if the inputs are integers
    if not (isinstance(a, int) and isinstance(b, int)):
        return "Error: Both a and b must be integers."

    # Checking if the operation is supported
    if operation not in ['add', 'subtract', 'multiply', 'divide']:
        return "Error: operation must be either 'add', 'subtract', 'multiply' or 'divide'."

    # Calculations
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        # Checking if denominator is zero
        if b == 0:
            return "Error: Cannot divide by zero."
        else:
            return a / b