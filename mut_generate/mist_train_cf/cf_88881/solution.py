"""
QUESTION:
Implement a function `search(arr, target)` that uses interpolation search to find the index of a given `target` element in a sorted array `arr`. If the `target` element is not present in the array, return `-1`. The function should handle arrays with duplicate elements, returning the index of any occurrence. The time complexity should be `O(log(log(n)))` and space complexity should be `O(1)`, where `n` is the length of the array.
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