"""
QUESTION:
Create a function `remove_target_value(lst, target)` that takes a list of integers `lst` and a target value `target`, and returns a new list with all occurrences of the target value removed. The function should not modify the original list, have a time complexity of O(n), and a space complexity of O(n), where n is the length of the list.
"""

def remove_target_value(lst, target):
    """
    Removes all occurrences of the target value from the given list.
    
    Args:
        lst (list): A list of integers.
        target (int): The target value to be removed.
    
    Returns:
        list: A new list with all occurrences of the target value removed.
    """
    return [num for num in lst if num != target]