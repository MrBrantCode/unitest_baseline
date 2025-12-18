"""
QUESTION:
Create a function called `binary_search` that performs a binary search on a sorted list of integers. The function should take two parameters: a sorted list of integers and a target integer to search for. The function should return the index of the first occurrence of the target integer if it exists in the list, or -1 if it does not. The list may contain duplicate integers, and the function should be able to handle this case correctly.
"""

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            if mid == 0 or arr[mid - 1] != target:
                return mid
            else:
                end = mid - 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return -1