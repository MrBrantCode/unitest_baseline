"""
QUESTION:
Write a function named `binary_search` that performs a binary search on a sorted list of integers to find the starting and ending indexes of all occurrences of a target value. The list can contain both positive and negative integers and is sorted in non-decreasing order. The function should return a tuple containing the starting and ending indexes if the target value is found. If the target value is not found, the function should return the message "The target value is not found in the list". The function should achieve O(log n) time complexity in searching.
"""

def binary_search(mylist, target):
    """
    Performs a binary search on a sorted list of integers to find the starting and ending indexes of all occurrences of a target value.
    
    Args:
        mylist (list): A sorted list of integers.
        target (int): The target value to be searched.
    
    Returns:
        tuple: A tuple containing the starting and ending indexes if the target value is found. Otherwise, returns the message "The target value is not found in the list".
    """

    low, high = 0, len(mylist) - 1

    while low <= high:
        mid = (high + low) // 2
        if mylist[mid] < target:
            low = mid + 1
        elif mylist[mid] > target:
            high = mid - 1
        else:
            start = end = mid
            while start > 0 and mylist[start - 1] == target:
                start -= 1
            while end < len(mylist) - 1 and mylist[end + 1] == target:
                end += 1
            return (start, end)

    return "The target value is not found in the list"