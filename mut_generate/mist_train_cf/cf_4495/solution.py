"""
QUESTION:
Write a function named `product_of_perfect_squares` that takes a 2D array as input, calculates the product of all perfect square elements in the array, and returns the result if the product does not exceed 10^9; otherwise, return -1.
"""

def product_of_perfect_squares(arr):
    """
    Calculate the product of all perfect square elements in a 2D array.

    Args:
    arr (list): A 2D list of integers.

    Returns:
    int: The product of all perfect square elements if it does not exceed 10^9; otherwise, -1.
    """
    product = 1
    for row in arr:
        for element in row:
            if element > 0 and int(element ** 0.5) ** 2 == element:  # check if element is a perfect square
                product *= element
                if product > 10**9:  # check if product exceeds 10^9
                    return -1
    return product