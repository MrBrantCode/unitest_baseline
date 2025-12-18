"""
QUESTION:
Create a function named `multiply` that takes two numbers `x` and `y` as arguments and returns their product without using the multiplication operator or any built-in functions that directly calculate the product of two numbers. Implement the logic using basic arithmetic operations such as addition, subtraction, and division.
"""

def multiply(x, y):
    # Initialize the product to 0
    product = 0

    # Determine the sign of the product
    sign = 1
    if x < 0:
        x = -x
        sign = -sign
    if y < 0:
        y = -y
        sign = -sign

    # Calculate the product using repeated addition
    while y > 0:
        if y % 2 == 1:
            product += x
        x += x
        y //= 2

    # Apply the sign to the product
    product *= sign

    return product