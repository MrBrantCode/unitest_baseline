"""
QUESTION:
Create a function named `remove_duplicates` that takes a list of integers as input and returns a new list with all duplicates removed. The function must have a time complexity of O(n log n) or better.
"""

def remove_duplicates(nums):
    """
    Removes duplicates from a list of integers.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A new list with all duplicates removed.
    """
    nums.sort()
    unique_list = []
    for i in range(len(nums)):
        if i == len(nums) - 1 or nums[i] != nums[i + 1]:
            unique_list.append(nums[i])
    return unique_list