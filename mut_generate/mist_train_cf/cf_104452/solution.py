"""
QUESTION:
Create a function `combine_sorted_arrays` that takes two arrays `arr1` and `arr2` as input. The function should remove duplicate elements from both arrays, combine them into a single array, and return the combined array in ascending order. The input arrays are of the same size.
"""

def combine_sorted_arrays(arr1, arr2):
    """
    Combine two arrays into a single array, removing duplicates and sorting in ascending order.

    Args:
        arr1 (list): The first array.
        arr2 (list): The second array.

    Returns:
        list: The combined array.
    """
    # Remove duplicate elements from both arrays and concatenate them
    combined_array = list(set(arr1 + arr2))
    
    # Sort the combined array in ascending order
    return sorted(combined_array)