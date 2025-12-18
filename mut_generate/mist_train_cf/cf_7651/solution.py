"""
QUESTION:
Create a function called `multiply_and_check_divisibility(a, b)` that takes two numbers as input, multiplies them together, and checks if the result is divisible by 3. The function should only accept positive integers greater than zero and should return an error message if either input is not a positive integer. If the inputs are floating-point numbers, the function should round the result to the nearest integer. The function should return the result and a message stating whether it is divisible by 3 or not.
"""

def multiply_and_check_divisibility(a, b):
    """
    This function multiplies two numbers together, checks if the result is divisible by 3,
    and returns the result with a corresponding message.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        str: The result and a message stating whether it is divisible by 3 or not.
    """

    # Check if both inputs are positive and greater than zero
    if a <= 0 or b <= 0:
        return "Error: Both input numbers must be positive and greater than zero."

    # Check if both inputs are integers (if not, round the result to the nearest integer)
    if not isinstance(a, int) or not isinstance(b, int):
        a = round(a)
        b = round(b)

    # Calculate the result
    result = a * b

    # Check if the result is divisible by 3
    if result % 3 == 0:
        return f"The result {result} is divisible by 3."
    else:
        return f"The result {result} is not divisible by 3."