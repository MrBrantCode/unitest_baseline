"""
QUESTION:
Write a function `sub_arrays(array)` that takes an array of integers as input and returns the total number of unique subarrays. A subarray is an array that can be obtained from the given array by deleting any number of elements from the beginning or the end. The function should not include the empty subarray in the count.
"""

def sub_arrays(array):
    """
    Calculate the total number of unique subarrays.
    
    Args:
    array (list): A list of integers.
    
    Returns:
    int: The total number of unique subarrays.
    """
    subarr = [[]]
    for i in range(len(array)):
        for j in range(i + 1, len(array) + 1):
            sub = array[i:j]
            subarr.append(sub)
    return len(set(tuple(x) for x in subarr)) - 1