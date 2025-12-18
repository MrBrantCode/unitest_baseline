"""
QUESTION:
Implement a function named `mergeSort` that sorts a given array of integers in ascending order, with a time complexity of O(n log n) and a space complexity of O(1). The function should not use any built-in sorting functions or libraries and should handle duplicate integers, negative integers, and arrays containing only negative integers. The original array should remain unchanged, and the sorted array should be stored in a new array.
"""

def mergeSort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    
    def merge(left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    left = mergeSort(left)
    right = mergeSort(right)
    
    return merge(left, right)