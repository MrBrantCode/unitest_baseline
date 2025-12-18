"""
QUESTION:
Write a function named "multiply_two_numbers" that takes two integer parameters, "a" and "b", within the range of -1000 to 1000. The function should return the product of "a" and "b". If either "a" or "b" is not an integer or out of range, the function should return an error message. If the product is a floating-point number, the function should round it to the nearest integer before returning.
"""

def multiply_two_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return "Error: Both inputs must be integers."
    if not (-1000 <= a <= 1000) or not (-1000 <= b <= 1000):
        return "Error: Inputs must be within the range of -1000 to 1000."
    result = a * b
    if isinstance(result, float):
        result = round(result)
    return result