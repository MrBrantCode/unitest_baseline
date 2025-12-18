"""
QUESTION:
Implement a function `search_element(arr, target)` that finds the indices of all occurrences of a target element in a sorted array `arr` that can contain duplicates. The function should return a list of indices where the target element is found. If the element is not found, return an empty list. The time complexity of the function should be O(log n) in the worst case scenario, and the array size can be up to 10^6.
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