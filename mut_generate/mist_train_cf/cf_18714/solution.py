"""
QUESTION:
Generate a function named 'pairwise_combinations_with_sum' that takes a list of integers as input and returns a list of tuples. Each tuple should contain a pairwise combination of the input numbers and the sum of those two numbers. The function should exclude any duplicate combinations.
"""

def pairwise_combinations_with_sum(nums):
    """
    Generate a list of tuples containing pairwise combinations of input numbers and their sum.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A list of tuples, each containing a pairwise combination of input numbers and their sum.
    """
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            result.append(((nums[i], nums[j]), nums[i] + nums[j]))
    return result