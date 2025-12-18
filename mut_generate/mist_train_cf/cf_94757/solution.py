"""
QUESTION:
Implement a function `binary_search_recursive(data, target, low, high)` that uses the binary search algorithm recursively to find the index of the first occurrence of the target number in a sorted data list. The function should return -1 if the target number is not found. The input data list should be sorted and the function should have a time complexity of O(log n), where n is the size of the data list.
"""

def binary_search_recursive(data, target, low, high):
    # Base case: target number not found
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    # If the target number is found, check if it's the first occurrence
    if data[mid] == target:
        if mid == 0 or data[mid-1] != target:
            return mid
        else:
            return binary_search_recursive(data, target, low, mid-1)
    
    # If the target number is smaller, search in the left half
    elif data[mid] > target:
        return binary_search_recursive(data, target, low, mid-1)
    
    # If the target number is larger, search in the right half
    else:
        return binary_search_recursive(data, target, mid+1, high)