"""
QUESTION:
Write a function called `merge_and_sort_arrays` that takes two lists of integers as input and returns a new list that contains all unique elements from both lists in ascending order. The input lists can contain duplicate elements and are not guaranteed to be sorted. The function should not modify the original lists.
"""

def merge_and_sort_arrays(array1, array2):
    """
    Merge two lists of integers into one, removing duplicates and sorting in ascending order.

    Args:
        array1 (list): The first list of integers.
        array2 (list): The second list of integers.

    Returns:
        list: A new list containing unique elements from both input lists in ascending order.
    """
    # Merge the two arrays
    merged_array = array1 + array2
    
    # Remove duplicate elements from the merged array
    merged_array = list(set(merged_array))
    
    # Sort the merged array in ascending order
    merged_array.sort()
    
    return merged_array