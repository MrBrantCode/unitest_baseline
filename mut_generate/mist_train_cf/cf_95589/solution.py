"""
QUESTION:
Write a function `product_of_perfect_squares` that calculates the product of all perfect square elements in a given two-dimensional array. The input array contains integers, and the function should return an integer representing the product of the perfect square elements. The input array can be empty or contain no perfect squares.
"""

def product_of_perfect_squares(arr):
    """
    This function calculates the product of all perfect square elements in a given two-dimensional array.

    Args:
        arr (list): A two-dimensional array of integers.

    Returns:
        int: The product of the perfect square elements in the array.
    """
    product = 1
    for sublist in arr:
        for num in sublist:
            if int(num**0.5)**2 == num:  # Check if the number is a perfect square
                product *= num
    return product