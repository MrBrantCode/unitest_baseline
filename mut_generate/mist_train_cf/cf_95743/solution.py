"""
QUESTION:
Write a function `count_occurrences` that returns the number of times a target element appears in a sorted array. The function should only use a single loop and have a time complexity of O(log n), where n is the size of the array. The array will contain at most 10^9 elements and the target element will be a positive integer between 1 and 10^9 inclusive. The function should handle duplicate elements in the array efficiently.
"""

def count_occurrences(arr, target):
    def find_first_occurrence(arr, target):
        low = 0
        high = len(arr) - 1
        result = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == target:
                result = mid
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return result

    def find_last_occurrence(arr, target):
        low = 0
        high = len(arr) - 1
        result = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == target:
                result = mid
                low = mid + 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return result

    first = find_first_occurrence(arr, target)
    last = find_last_occurrence(arr, target)
    
    if first == -1 or last == -1:
        return 0
    
    return last - first + 1