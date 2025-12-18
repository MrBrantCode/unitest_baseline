"""
QUESTION:
Design a function called `consecutive_product` that calculates the product of consecutive elements in a given tuple until the product exceeds a specified target limit. The function should return the product of the consecutive elements that do not exceed the target limit.

The input tuple contains integers and the target limit is a positive integer. The function should start multiplying from the first element of the tuple and continue until the product exceeds the target limit. If the target limit is less than the first element of the tuple, the function should return 1.
"""

def consecutive_product(nums, target):
    """
    Calculate the product of consecutive elements in a tuple until the product exceeds a target limit.

    Args:
    nums (tuple): A tuple of integers.
    target (int): A positive integer target limit.

    Returns:
    int: The product of consecutive elements that do not exceed the target limit.
    """
    product = 1
    for num in nums:
        if product * num <= target:
            product *= num
        else:
            break
    return product if product < target else 1