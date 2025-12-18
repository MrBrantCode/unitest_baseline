"""
QUESTION:
Create a function called `create_new_array` that takes a list of two numbers as input and returns a new list of four elements. The first element of the new list is the sum of the two input numbers, the second element is the difference between the two input numbers, the third element is the product of the two input numbers, and the fourth element is the quotient of the two input numbers, with the first input number as the dividend.
"""

def create_new_array(numbers):
    """
    This function takes a list of two numbers as input and returns a new list of four elements.
    The new list contains the sum, difference, product, and quotient of the input numbers.
    
    Args:
        numbers (list): A list of two numbers.
    
    Returns:
        list: A new list with four elements.
    """
    return [
        numbers[0] + numbers[1],  # sum of the two input numbers
        numbers[0] - numbers[1],  # difference between the two input numbers
        numbers[0] * numbers[1],  # product of the two input numbers
        numbers[0] / numbers[1]   # quotient of the two input numbers
    ]