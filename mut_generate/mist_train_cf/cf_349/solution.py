"""
QUESTION:
Implement a function `optimized_sort(arr)` that takes an array `arr` as input and returns a new array with the elements sorted in ascending order, without any duplicates. The sorting algorithm used should have a time complexity of O(n log n). You cannot use any built-in sorting functions or libraries.
"""

def optimized_sort(arr):
    def merge_sort(arr):
        # Base case
        if len(arr) <= 1:
            return arr
        
        # Divide the array into two halves
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        # Recursively sort the two halves
        left = merge_sort(left)
        right = merge_sort(right)
        
        # Merge the sorted halves
        return merge(left, right)
    
    def merge(left, right):
        merged = []
        i = 0
        j = 0
        
        # Compare and merge the elements from left and right halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            elif left[i] > right[j]:
                merged.append(right[j])
                j += 1
            else:
                merged.append(left[i])
                i += 1
                j += 1
        
        # Append the remaining elements
        while i < len(left):
            merged.append(left[i])
            i += 1
        
        while j < len(right):
            merged.append(right[j])
            j += 1
        
        return merged
    
    # Remove duplicates by converting to set and back to list
    arr = list(set(arr))
    
    # Sort the array using merge sort
    return merge_sort(arr)