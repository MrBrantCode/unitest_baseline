"""
QUESTION:
Implement a function named `product_of_even_numbers` to calculate the product of all non-negative, even elements in a given list. The function should handle empty lists and negative numbers, and return the product as a result.
"""

def product_of_even_numbers(num_list):
    """
    Calculate the product of all non-negative, even elements in a given list.

    Args:
    num_list (list): A list of integers.

    Returns:
    int: The product of non-negative, even elements in the list.
    """
    product = 1
    for num in num_list:
        if num >= 0 and num % 2 == 0:
            product *= num
    return product