"""
QUESTION:
Implement a function `binary_search` that performs a binary search on a sorted array to find the index of a target element. The function should have a runtime complexity of O(log n) and handle arrays with duplicate elements. The function should take four parameters: `arr` (the sorted array), `low` (the starting index of the search range), `high` (the ending index of the search range), and `target` (the target element to be searched). The function should return the index of the target element if found, or -1 if not found.
"""

def binary_search(arr, low, high, target):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    
    if arr[low] < arr[mid] or (arr[low] == arr[mid] and arr[mid] != arr[high]):
        if arr[low] <= target < arr[mid]:
            return binary_search(arr, low, mid - 1, target)
        return binary_search(arr, mid + 1, high, target)
    
    if arr[mid] < arr[high] or (arr[mid] == arr[high] and arr[low] != arr[mid]):
        if arr[mid] < target <= arr[high]:
            return binary_search(arr, mid + 1, high, target)
        return binary_search(arr, low, mid - 1, target)
    
    if arr[low] == arr[mid]:
        result = binary_search(arr, low, mid - 1, target)
        if result == -1:
            return binary_search(arr, mid + 1, high, target)
        return result
    
    return -1