"""
QUESTION:
Write a function `remove_duplicates(arr)` that takes an array of integers as input and returns a new array with all duplicate elements removed while maintaining their original order. The time complexity of the solution should be O(n), where n is the length of the array.
"""

def remove_duplicates(arr):
    """
    Remove duplicates from the array while maintaining their original order.

    Args:
        arr (list): The input array of integers.

    Returns:
        list: A new array with all duplicate elements removed.
    """
    unique_set = set()
    unique_arr = []

    for num in arr:
        if num not in unique_set:
            unique_set.add(num)
            unique_arr.append(num)

    return unique_arr