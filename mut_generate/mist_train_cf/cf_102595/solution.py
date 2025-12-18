"""
QUESTION:
Write a function named `delete_and_sum` that takes a list of integers as input, deletes all items with a value of 3, and returns the sum of the remaining items. The function should handle edge cases where the input list is empty or contains only items with a value of 3.
"""

def delete_and_sum(nums):
    """
    This function deletes all items with a value of 3 in a given list and returns the sum of the remaining items.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The sum of the remaining items after deleting all items with a value of 3.
    """
    # Check if the list is empty or contains only items with a value of 3
    if not nums or all(item == 3 for item in nums):
        return 0
    else:
        # Delete all items with a value of 3 and return the sum of the remaining items
        return sum(item for item in nums if item != 3)