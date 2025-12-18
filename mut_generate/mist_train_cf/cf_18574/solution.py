"""
QUESTION:
Create a function `reindex_array` that reindexes the values of a given array with their corresponding indices. The function must not use any built-in indexing functions or libraries, must be implemented using a single loop, and cannot use any additional variables or data structures.
"""

def reindex_array(arr):
    """
    Reindexes the values of a given array with their corresponding indices.

    Args:
        arr (list): The input array to be reindexed.

    Returns:
        list: The reindexed array.
    """
    for i in range(len(arr)):
        arr[i] = i
    return arr