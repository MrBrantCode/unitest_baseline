"""
QUESTION:
Implement a `search` function that takes a sorted array `arr` and a target element `target` as input, and returns the index of the target element if it exists in the array. If the target element is not present, return -1. The function should have a time complexity of O(log(log(n))) and a space complexity of O(1), where n is the length of the array. The function should handle arrays with duplicate elements and return the index of any occurrence of the target element.
"""

def search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + int((float(high - low) / (arr[high] - arr[low])) * (target - arr[low]))
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    
    return -1