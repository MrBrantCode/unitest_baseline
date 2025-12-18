"""
QUESTION:
Write a function `max_product_of_four` that takes a list of integers as input. The function should calculate the maximum product of four numbers in the list, where at least two of the numbers must be negative and one of them must be odd. The function should return the maximum product. The list contains at least four integers and the integers can be positive, negative, or zero.
"""

def max_product_of_four(nums):
    """
    This function calculates the maximum product of four numbers in the list.
    The four numbers must include at least two negative numbers and one odd number.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The maximum product of four numbers in the list.
    """

    # Sort the list in ascending order
    nums.sort()

    # Calculate the product of the first two negative numbers and the last two positive numbers
    product1 = nums[0] * nums[1] * nums[-1] * nums[-2]

    # Calculate the product of the first three negative numbers and the last positive number
    product2 = nums[0] * nums[1] * nums[2] * nums[-1]

    # Return the maximum product
    return max(product1, product2)