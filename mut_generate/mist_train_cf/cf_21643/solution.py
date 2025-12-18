"""
QUESTION:
Write a function `isSortedDescending` that takes an array of integers as input. This function should return two values: a boolean indicating whether the input array is sorted in descending order, and the count of distinct elements in the array. The function should assume that the array can contain duplicate elements. The time complexity should be O(n log n) due to the need to sort the array to remove duplicates.
"""

def isSortedDescending(array):
    """
    This function checks if the input array is sorted in descending order 
    and returns the count of distinct elements in the array.

    Args:
        array (list): A list of integers.

    Returns:
        tuple: A boolean indicating whether the array is sorted in descending order, 
               and the count of distinct elements in the array.
    """

    isDescending = all(array[i] >= array[i+1] for i in range(len(array)-1))
    sorted_array = sorted(array)
    distinct_count = len(set(sorted_array))

    return isDescending, distinct_count