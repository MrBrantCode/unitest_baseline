"""
QUESTION:
Write a function `binary_search` that performs a binary search within a pre-sorted list of negative and non-negative integers. The function should identify and print out all duplicate values found during the search for a specific item. The function should take four parameters: a sorted list `arr`, the lower and upper bounds `low` and `high`, and the target `item`. If the item is found, the function should return its index; otherwise, it should return -1.
"""

def binary_search(arr, low, high, item):
    """
    Performs binary search within a pre-sorted list of integers and identifies duplicate values.
    
    Parameters:
    arr (list): A sorted list of integers.
    low (int): The lower bound of the search range.
    high (int): The upper bound of the search range.
    item (int): The target item to search for.
    
    Returns:
    int: The index of the item if found, -1 otherwise.
    """
    if low <= high:
        mid = (high + low) // 2
        if arr[mid] == item:
            if item in arr[mid + 1: high + 1] or item in arr[low: mid]:  
                print("Duplicate item found: ", item)
            return mid
        elif arr[mid] > item:
            return binary_search(arr, low, mid - 1, item)
        else:
            return binary_search(arr, mid + 1, high, item)
    else:
        return -1