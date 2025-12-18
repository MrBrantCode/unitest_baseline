"""
QUESTION:
Design a function named `merge_sort` that sorts a list of integers in descending order without using built-in sorting functions or libraries. The function should have a time complexity of O(n log n) and a space complexity of O(1), and it should be stable, meaning that the order of equal elements is preserved.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide the list into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort the left and right halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Merge the sorted halves into a single sorted list
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Append the remaining elements of the left or right half
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result