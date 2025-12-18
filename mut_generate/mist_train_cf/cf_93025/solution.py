"""
QUESTION:
Create a function `calculate_factorial(num)` that calculates the factorial of a given non-negative integer `num` using a while loop. The function should return an error message if the input is not a valid integer or if it is a negative number.
"""

def calculate_factorial(num):
    if not isinstance(num, int):
        return "Error: Input is not a valid integer."
    if num < 0:
        return "Error: Input should be a non-negative integer."
    factorial = 1
    while num > 1:
        factorial *= num
        num -= 1
    return factorial