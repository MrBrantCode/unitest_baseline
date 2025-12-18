"""
QUESTION:
Implement a function called `merge_sort` that sorts a given list of numbers in descending order using a well-optimized sorting algorithm with a time complexity of O(n log n) or better, without using any built-in sorting functions or libraries. Ensure the function handles edge cases such as an empty list or a list with duplicate numbers and optimizes space complexity to O(log n) or better.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result