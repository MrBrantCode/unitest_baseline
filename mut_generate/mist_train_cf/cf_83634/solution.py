"""
QUESTION:
Create a function called `calculate_gcd` that takes two parameters, `num1` and `num2`. The function should compute the greatest common divisor (GCD) of `num1` and `num2` using the Euclidean algorithm, but only if both `num1` and `num2` are positive integers. The function should handle exceptions and errors, returning an error message if either `num1` or `num2` is not a positive integer.
"""

def calculate_gcd(num1, num2):
    try:
        num1, num2 = int(num1), int(num2)
    except ValueError:
        return "Error: Both inputs must be integers."
    if num1 < 1 or num2 < 1:
        return "Error: Both inputs must be positive."
    while(num2):
        num1, num2 = num2, num1 % num2
    return num1