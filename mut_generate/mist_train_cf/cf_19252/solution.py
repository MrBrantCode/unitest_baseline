"""
QUESTION:
Write a function `product_of_perfect_squares` that takes a two-dimensional array of integers as input and returns the product of all elements that are perfect squares.
"""

def product_of_perfect_squares(arr):
    """
    This function calculates the product of all elements that are perfect squares in a two-dimensional array.

    Args:
        arr (list): A two-dimensional array of integers.

    Returns:
        int: The product of all perfect square elements in the array.
    """
    product = 1
    for sublist in arr:
        for num in sublist:
            if int(num**0.5)**2 == num:  # Check if the number is a perfect square
                product *= num
    return product