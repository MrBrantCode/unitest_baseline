"""
QUESTION:
Write a function `max_product_of_three` that takes an array of integers as input and returns the maximum product of three numbers in the array, with the condition that at least one of the numbers must be negative. If no such triplet exists, return 0.
"""

def max_product_of_three(nums):
    """
    This function calculates the maximum product of three numbers in an array, 
    with the condition that at least one of the numbers must be negative. 
    If no such triplet exists, it returns 0.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The maximum product of three numbers in the array.
    """

    # Sort the array in ascending order
    nums.sort()

    # Calculate the product of the three largest numbers in the sorted array
    product1 = nums[-1] * nums[-2] * nums[-3]

    # Calculate the product of the two smallest numbers (which are negative) and the largest number
    product2 = nums[0] * nums[1] * nums[-1]

    # Return the maximum product
    return max(product1, product2) if nums[0] < 0 else 0