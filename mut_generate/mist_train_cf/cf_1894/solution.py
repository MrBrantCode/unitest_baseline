"""
QUESTION:
Write a function named `search_element` that takes a sorted array `arr` and a target element `target` as input and returns a list of indices where the target element appears in the array. If the target element is not found, return an empty list. The function must have a time complexity of O(log n) in the worst case scenario and should be able to handle arrays of up to 10^6 elements.
"""

def search_element(arr, target):
    start = 0
    end = len(arr) - 1
    indices = []
    
    while start <= end:
        middle = start + (end - start) // 2
        
        if arr[middle] == target:
            indices.append(middle)
            # Check for other occurrences to the left of middle
            i = middle - 1
            while i >= start and arr[i] == target:
                indices.append(i)
                i -= 1
            # Check for other occurrences to the right of middle
            i = middle + 1
            while i <= end and arr[i] == target:
                indices.append(i)
                i += 1
            return sorted(indices)
        
        elif target < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1
    
    return indices