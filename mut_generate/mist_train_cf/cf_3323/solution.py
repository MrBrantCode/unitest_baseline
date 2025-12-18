"""
QUESTION:
Create a function named "multiply_two_numbers" that takes two integer parameters "a" and "b" within the range of -1000 to 1000. The function should return the product of "a" and "b" if the input is valid. If the input is not valid, the function should return an error message. The function should handle cases where the input integers are negative, zero, or the result exceeds the range of integer values. If the result is a floating-point number, it should be rounded to the nearest integer.
"""

def multiply_two_numbers(a, b):
    """
    This function takes two integer parameters 'a' and 'b' within the range of -1000 to 1000.
    It returns the product of 'a' and 'b' if the input is valid, otherwise it returns an error message.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The product of 'a' and 'b' if the input is valid, otherwise an error message.
    """
    if not (isinstance(a, int) and isinstance(b, int)):
        return "Error: Both inputs must be integers."
    if not (-1000 <= a <= 1000 and -1000 <= b <= 1000):
        return "Error: Both inputs must be within the range of -1000 to 1000."
    
    product = round(a * b)
    if product < -1000 or product > 1000:
        return "Error: The result exceeds the range of integer values."
    
    return product