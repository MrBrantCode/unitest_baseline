"""
QUESTION:
Access and Binary Search on the Last Element of a Dynamic Array

Create a function that accesses and manipulates the last element of a dynamically sized array and performs a binary search on the last element. The array can be very large (up to 10^6 elements). The function should return the last element and its position in the array after binary search.

Restrictions: 
- The function should handle dynamic array size.
- The function should be efficient in terms of time complexity for accessing, manipulating, and performing binary search on the last element.
- The array can be very large (up to 10^6 elements).
- The array should be sorted before performing binary search.
"""

import bisect

def access_and_binary_search_last_element(arr):
    """
    Access and manipulate the last element of a dynamic array and perform a binary search on the last element.
    
    Args:
    arr (list): A dynamic array of elements.
    
    Returns:
    tuple: A tuple containing the last element and its position in the array after binary search.
    """
    
    # Check if the array is empty
    if not arr:
        return None, None

    # Access the last element in the array
    last_element = arr[-1]

    # Manipulate the last element in the array if needed
    # arr[-1] = 'New element'

    # Sort the array before performing binary search
    arr.sort()

    # Binary search to find the position of last element in the array
    pos = bisect.bisect_left(arr, last_element)

    return last_element, pos