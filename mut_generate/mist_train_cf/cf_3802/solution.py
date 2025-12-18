"""
QUESTION:
Create a function called `filtered_nums` that takes a list of integers as input. The function should return a list of numbers that are divisible by 3 and not divisible by 4. The resulting list should be sorted in descending order and have all duplicate values removed. The function must have a time complexity of O(n), where n is the number of elements in the input list.
"""

def filtered_nums(nums):
    """
    Returns a list of numbers from the input list that are divisible by 3 and not divisible by 4.
    The resulting list is sorted in descending order with no duplicates.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A list of integers that meet the specified conditions.
    """
    return sorted(list(set([x for x in nums if x % 3 == 0 and x % 4 != 0])), reverse=True)