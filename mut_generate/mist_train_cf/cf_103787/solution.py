"""
QUESTION:
Implement a function named `binary_search` that takes in a sorted list of integers and a target integer as parameters. The function should perform a binary search to find the target element in the list and return the element along with its index if found; otherwise, it should return `None` for both the element and index. The list is guaranteed to be sorted in ascending order.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_element = arr[mid]
        
        if mid_element == target:
            return mid_element, mid
        elif mid_element < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return None, None