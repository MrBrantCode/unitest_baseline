"""
QUESTION:
Implement a function `binary_search` that performs a binary search on a list of integers to find a target element, returning the path taken and the index of the target element if found. The list may contain both unique and non-unique elements, and the function should return the first occurrence of the target element. If the list is not sorted, it should be sorted in ascending order before performing the binary search. If the target element is not found, return a message indicating it's not found along with the path taken. The function should work for both sorted and unsorted input lists.
"""

def binary_search(lst, target):
    """
    Performs a binary search on a list of integers to find a target element, 
    returning the path taken and the index of the target element if found.

    Args:
        lst (list): A list of integers.
        target (int): The target element to be found.

    Returns:
        tuple: A tuple containing the index of the target element if found, 
               along with the path taken. If the target element is not found, 
               returns a message indicating it's not found along with the path taken.
    """
    lst.sort()  # Sort the list in ascending order
    start = 0
    end = len(lst) - 1
    path = []

    while start <= end:
        mid = start + (end - start) // 2
        path.append(lst[mid])
        
        if lst[mid] == target:
            return f"Target found at index position {mid}, Path: {path}"
        elif lst[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return f"Target not found!, Path: {path}"