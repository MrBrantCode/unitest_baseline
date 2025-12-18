"""
QUESTION:
Write a function named `multiply` that takes two parameters `x` and `y` and calculates the product of these two numbers without using the multiplication operator. The solution must involve the use of loops and conditional statements. The function should handle cases where one or both of the inputs are 0 and should consider the sign of the inputs, returning a negative result when necessary. Additionally, validate the input to ensure it's a number.
"""

def multiply(x, y):
    """
    Calculate the product of two numbers without using the multiplication operator.

    This function takes two parameters, x and y, and returns their product. It handles cases where one or both of the inputs are 0 and considers the sign of the inputs, returning a negative result when necessary.

    :param x: The first number
    :param y: The second number
    :return: The product of x and y
    """

    # Initialize the result
    result = 0

    # Check if 'x' is 0. Since, 0 multiplied by any number is 0.
    if x == 0:
        return 0

    # Check if 'y' is 0. Since, 0 multiplied by any number is 0.
    elif y == 0:
        return 0

    # Checking for negative numbers and making them positive for simplification
    elif x < 0:
        x = -x
        y = -y

    # Using a loop to add 'x' to the result, 'y' times.
    for _ in range(abs(y)):
        result += x

    # Return the product
    if (x < 0 and y < 0) or (x > 0 and y > 0):
        return result
    else:
        return -result