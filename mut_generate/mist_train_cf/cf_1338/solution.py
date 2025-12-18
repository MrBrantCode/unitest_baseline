"""
QUESTION:
Create a function called `remove_target_value` that takes in two parameters: a list of integers and a target integer. Return a new list with all occurrences of the target integer removed. The function should have a time complexity of O(n), where n is the length of the list, but it does not have to meet the O(1) space complexity requirement as the given answer does not meet this requirement as well.
"""

def remove_target_value(nums, target):
    """
    Removes all occurrences of a target integer from a list of integers.

    Args:
        nums (list): A list of integers.
        target (int): The target integer to be removed.

    Returns:
        list: A new list with all occurrences of the target integer removed.
    """
    removed_list = []
    for num in nums:
        if num != target:
            removed_list.append(num)
    return removed_list