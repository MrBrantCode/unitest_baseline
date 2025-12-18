"""
QUESTION:
Write a function called `remove_duplicates_and_limit` that takes an array of integers `arr` and an integer `limit` (1 <= limit <= 10^4) as input, removes all duplicate elements from the array, removes elements that exceed the `limit`, and returns the new array. Note that the order of elements in the original array may not be preserved.
"""

def remove_duplicates_and_limit(arr, limit):
    """
    Removes all duplicate elements from the array and elements that exceed the limit.

    Args:
    arr (list): The input array of integers.
    limit (int): The maximum value for elements in the array.

    Returns:
    list: A new array with duplicates removed and elements not exceeding the limit.
    """
    return list(set([x for x in arr if x <= limit]))