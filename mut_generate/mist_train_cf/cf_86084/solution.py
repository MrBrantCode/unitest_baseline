"""
QUESTION:
Write a function named `find_first_and_last_occurrence` that takes a list of integers `nums` and a target integer `target` as input. The function should return the indices of the first and last occurrence of the target value in the list. If the target value is not present in the list, the function should return a message indicating that the target value is not in the list.
"""

def find_first_and_last_occurrence(nums, target):
    """
    Returns the indices of the first and last occurrence of the target value in the list.

    Args:
        nums (list): A list of integers.
        target (int): The target integer to find.

    Returns:
        tuple: A tuple containing the indices of the first and last occurrence of the target value. 
               If the target value is not present in the list, returns a message indicating that the target value is not in the list.
    """
    first_occurrence = None
    last_occurrence = None

    for i, num in enumerate(nums):
        if num == target:
            if first_occurrence is None:
                first_occurrence = i
            last_occurrence = i

    if first_occurrence is None:
        return 'Target value is not in the list.'
    else:
        return first_occurrence, last_occurrence