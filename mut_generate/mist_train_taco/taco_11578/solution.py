"""
QUESTION:
You are given two sorted arrays that contain only integers. Your task is to find a way to merge them into a single one, sorted in **ascending order**. Complete the function `mergeArrays(arr1, arr2)`, where `arr1` and `arr2` are the original sorted arrays.

You don't need to worry about validation, since `arr1` and `arr2` must be arrays with 0 or more Integers. If both `arr1` and `arr2` are empty, then just return an empty array.

**Note:** `arr1` and `arr2` may be sorted in different orders. Also `arr1` and `arr2` may have same integers. Remove duplicated in the returned result.

## Examples

Happy coding!
"""

def merge_sorted_arrays(arr1, arr2):
    """
    Merges two sorted arrays of integers into a single sorted array with duplicates removed.

    Parameters:
    arr1 (list of int): The first sorted array of integers.
    arr2 (list of int): The second sorted array of integers.

    Returns:
    list of int: A sorted array of integers that merges arr1 and arr2, with duplicates removed.
    """
    return sorted(set(arr1 + arr2))