"""
QUESTION:
Implement a function named `custom_sort_descending` that takes an array of integers as input, removes duplicate elements, and returns the unique elements in descending order without using built-in sorting functions.
"""

def custom_sort_descending(arr):
    """
    This function takes an array of integers, removes duplicates, 
    and returns unique elements in descending order without using built-in sorting functions.

    Args:
        arr (list): The input list of integers.

    Returns:
        list: A list of unique integers in descending order.
    """

    # Implement bubble sort
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    
    # Remove duplicates
    unique_elements = []
    for i in range(len(arr)):
        if arr[i] not in unique_elements:
            unique_elements.append(arr[i])
    
    return unique_elements