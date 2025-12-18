"""
QUESTION:
Implement a function `linear_search(array, target)` that performs a linear search on the input array to find the index of the target number. The array will contain 10,000,000 random integers between -10,000,000 and 10,000,000, and the target number will be a prime number between 1,000,000 and 10,000,000. If the target number is found, return its index; otherwise, return -1.
"""

def linear_search(array, target):
    """
    Perform a linear search on the input array to find the index of the target number.

    Args:
        array (list): A list of integers.
        target (int): The target number to be searched.

    Returns:
        int: The index of the target number if found, -1 otherwise.
    """
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1