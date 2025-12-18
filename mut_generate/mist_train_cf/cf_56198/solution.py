"""
QUESTION:
Create a function named `product_remainder_3` that takes a list of integers as input. The function should identify the elements in the list where the remainder when divided by 3 is 1, then return the product of these elements.
"""

def product_remainder_3(nums):
    """
    This function calculates the product of numbers in a list that have a remainder of 1 when divided by 3.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The product of numbers with a remainder of 1 when divided by 3.
    """
    product = 1
    for num in nums:
        if num % 3 == 1:
            product *= num
    return product