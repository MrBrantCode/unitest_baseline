"""
QUESTION:
Write a function, `generate_sorted_sums`, that takes two lists of 50 integers each and returns a list of 100 elements. Each element in the returned list should be the sum of the corresponding elements in the input lists, and the elements in the returned list should be sorted in descending order.
"""

def generate_sorted_sums(arr1, arr2):
    """
    Generate a list of sums of corresponding elements in two input lists, sorted in descending order.

    Args:
        arr1 (list): The first list of integers.
        arr2 (list): The second list of integers.

    Returns:
        list: A list of sums of corresponding elements, sorted in descending order.
    """
    return sorted([x + y for x, y in zip(arr1, arr2)], reverse=True)