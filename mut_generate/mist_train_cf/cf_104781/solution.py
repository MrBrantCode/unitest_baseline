"""
QUESTION:
Write a function `filter_and_multiply` that takes a list of numbers as input and returns the product of the numbers that are not divisible by both 2 and 3. The function should ignore the numbers that are multiples of both 2 and 3, and calculate the product of the remaining numbers in the list. The input list contains only integers, and the function should return an integer as the product of the remaining numbers.
"""

def filter_and_multiply(numbers):
    """
    This function filters out numbers that are divisible by both 2 and 3 from the input list, 
    then returns the product of the remaining numbers.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The product of the numbers that are not divisible by both 2 and 3.
    """
    product = 1
    for num in numbers:
        if not (num % 2 == 0 and num % 3 == 0):
            product *= num
    return product