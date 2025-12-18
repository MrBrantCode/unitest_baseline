"""
QUESTION:
Create a function named count_unique that takes a sorted array and its size as input, and returns the number of unique elements in the array. The function should have a time complexity of O(n) or less and cannot use any additional data structures such as arrays, hash maps, or sets.
"""

def count_unique(array):
    """
    This function takes a sorted array as input and returns the number of unique elements in the array.

    Args:
        array (list): A sorted list of elements.

    Returns:
        int: The number of unique elements in the array.
    """
    if not array:
        return 0

    count = 1  # at least one unique element in the array
    for i in range(1, len(array)):
        if array[i] != array[i-1]:
            count += 1
    return count