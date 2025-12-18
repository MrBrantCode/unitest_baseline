"""
QUESTION:
Create a function called `create_triplets` that takes a list of integers as input and returns a list of lists, where each sublist contains three consecutive elements from the original list. The function should arrange the input list into triplets, stopping when there are not enough elements left to form a complete triplet.
"""

def create_triplets(nums):
    """
    This function takes a list of integers as input and returns a list of lists, 
    where each sublist contains three consecutive elements from the original list.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A list of lists, where each sublist contains three consecutive elements.
    """
    return [nums[n:n+3] for n in range(0, len(nums), 3)]