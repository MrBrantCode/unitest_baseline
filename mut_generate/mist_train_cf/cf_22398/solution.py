"""
QUESTION:
Remove all elements with a specified value from an array in-place. Given an array and an integer `val`, modify the array such that all elements equal to `val` are removed and the remaining elements are shifted to the left to fill the gap. The function should not use any additional data structures and the size of the original array should remain unchanged. The function should return the array after modification.

Function name: remove_element_in_place

Input: 
- arr (list of integers)
- val (integer to be removed)

Restriction: 
- The function should not use any additional data structures.
- The size of the original array should remain unchanged.
"""

def remove_element_in_place(arr, val):
    """
    Removes all elements with a specified value from an array in-place.
    
    Args:
    arr (list of integers): The input array.
    val (integer): The value to be removed.
    
    Returns:
    list of integers: The array after modification.
    """
    shift = 0
    for i in range(len(arr)):
        if arr[i] != val:
            arr[i - shift] = arr[i]
        else:
            shift += 1
    return arr