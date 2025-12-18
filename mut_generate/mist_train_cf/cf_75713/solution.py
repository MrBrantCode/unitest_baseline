"""
QUESTION:
Write a function `can_be_divided` that takes an array of integers as input and returns a boolean indicating whether the array can be divided into three segments with equal products. If no such arrangement is possible, the function should return `False`. The function should use a dynamic algorithm to solve the problem and should handle exceptions.
"""

from math import pow

def can_be_divided(arr):
    """
    This function determines whether an array of integers can be divided into three segments with equal products.

    Args:
        arr (list): A list of integers.

    Returns:
        bool: True if the array can be divided into three segments with equal products, False otherwise.
    """

    # Calculate the total product of the array
    total_product = 1
    for number in arr:
        total_product *= number

    # If total product is not a perfect cube, return False
    if not round(pow(total_product, 1.0/3)) ** 3 == total_product:
        return False

    # Calculate the target product which is cube root of total product
    target_product = round(pow(total_product, 1.0/3))

    # Traverse the array to identify if we can find three different segments whose products are equal to each other
    product_so_far = 1
    found_parts = 0
    for number in arr:
        product_so_far *= number
        if product_so_far == target_product:
            product_so_far = 1
            found_parts += 1

    # Return True if we found three segments with equal products and the remaining product is 1
    return found_parts == 3 and product_so_far == 1