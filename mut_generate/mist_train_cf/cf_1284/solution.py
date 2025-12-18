"""
QUESTION:
Implement a function named `binary_search` that uses a recursive approach to search for a target element in a sorted array with potential duplicate elements. The function should have a time complexity of O(log n) and handle the duplicate elements by searching both halves of the array when necessary. The function should take in parameters `arr` (the sorted array), `low` and `high` (the current search range), and `target` (the element to be searched).
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