"""
QUESTION:
Create a function `calculate` that performs the following operations: 
- Adds two numbers.
- Subtracts two numbers.
- Multiplies two numbers.
- Divides two numbers.
- Converts Celsius to Fahrenheit.
- Converts Fahrenheit to Celsius.

The function should take two arguments, `num1` and `num2`, and an optional argument `operation`. The `operation` can be one of `add`, `subtract`, `multiply`, `divide`, `celsius_to_fahrenheit`, `fahrenheit_to_celsius`. 

If the operation is not specified, the function should return an error message. If the operation is `celsius_to_fahrenheit` or `fahrenheit_to_celsius`, the function should only take one argument, `num1`, and ignore `num2`. 

The function should return the result of the operation.
"""

def calculate(num1, num2=None, operation=None):
    """
    Performs basic arithmetic operations and temperature conversions.

    Args:
    num1 (float): The first number.
    num2 (float, optional): The second number. Defaults to None.
    operation (str, optional): The operation to perform. Defaults to None.

    Returns:
    float: The result of the operation.
    """

    if operation is None:
        return "Error: Operation not specified."

    if operation == "add":
        if num2 is None:
            return "Error: Two numbers required for addition."
        return num1 + num2

    elif operation == "subtract":
        if num2 is None:
            return "Error: Two numbers required for subtraction."
        return num1 - num2

    elif operation == "multiply":
        if num2 is None:
            return "Error: Two numbers required for multiplication."
        return num1 * num2

    elif operation == "divide":
        if num2 is None or num2 == 0:
            return "Error: Two non-zero numbers required for division."
        return num1 / num2

    elif operation == "celsius_to_fahrenheit":
        if num2 is not None:
            return "Error: Only one number required for Celsius to Fahrenheit conversion."
        return (num1 * 9/5) + 32

    elif operation == "fahrenheit_to_celsius":
        if num2 is not None:
            return "Error: Only one number required for Fahrenheit to Celsius conversion."
        return (num1 - 32) * 5/9

    else:
        return "Error: Invalid operation."