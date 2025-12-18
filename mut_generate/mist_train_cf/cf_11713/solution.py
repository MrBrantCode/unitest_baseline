"""
QUESTION:
Implement a function named `sort_descending` that sorts an array of numbers in descending order. The function should take an array as input and return the sorted array. The function should not use any built-in sorting methods or libraries, and it should have a time complexity of O(n^2) or better.
"""

def sort_descending(array):
    """
    Sorts an array of numbers in descending order.

    Args:
        array (list): The input array of numbers.

    Returns:
        list: The sorted array in descending order.
    """
    swapped = True
    size = len(array)
    
    while swapped:
        swapped = False
        for i in range(size - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        size -= 1
    
    return array