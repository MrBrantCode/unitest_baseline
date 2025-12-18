"""
QUESTION:
Merge two arrays into one while maintaining the original order and keeping only unique elements. The merge should be case insensitive, meaning "Apple" and "apple" are considered the same element. If an element appears in both arrays, its position in the resultant array should correspond to its first appearance when both arrays are considered together.
"""

def merge_unique(arr1, arr2):
    """
    Merge two arrays into one while maintaining the original order and keeping only unique elements.
    The merge should be case insensitive, meaning "Apple" and "apple" are considered the same element.

    Args:
        arr1 (list): The first array.
        arr2 (list): The second array.

    Returns:
        list: The merged array with unique elements.
    """
    return arr1 + [item for item in arr2 if item.lower() not in [x.lower() for x in arr1]]


def remove_duplicates(arr):
    """
    Remove duplicates from an array while maintaining the original order.
    The removal is case insensitive, meaning "Apple" and "apple" are considered the same element.

    Args:
        arr (list): The input array.

    Returns:
        list: The array with duplicates removed.
    """
    res = []
    for item in arr:
        if item.lower() not in [x.lower() for x in res]:
            res.append(item)
    return res