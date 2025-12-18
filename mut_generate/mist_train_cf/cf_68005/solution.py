"""
QUESTION:
Implement a function `binary_search` that takes a sorted list of integers `arr`, the starting index `low`, the ending index `high`, and a target value `x` as input. The function should conduct a binary search for `x` in `arr` and return its index if found, or -1 if not found. The function should also handle exceptions. 

The input list `arr` will be sorted in ascending order before calling the `binary_search` function. The target value `x` will be a random integer within the range of the minimum and maximum values in `arr`.
"""

def binary_search(arr, low, high, x):
    """
    Conducts a binary search for a specific value.

    Parameters:
        arr (list): List in which is searched.
        low (int): Starting index in list.
        high (int): Ending index in list.
        x (int): Value to be searched.

    Returns:
        int: Index of found element or -1 if not found.
    """
    
    # Check base case
    if high >= low:
        mid = (high + low) // 2
  
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
  
        # If element is smaller than mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
  
        # Else the element is in right
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in array
        return -1