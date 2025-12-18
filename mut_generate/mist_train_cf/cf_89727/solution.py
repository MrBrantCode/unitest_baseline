"""
QUESTION:
Implement a function named `merge_sort` that takes a list of numbers as input and returns the sorted list in ascending order. You must implement the sorting algorithm yourself without using any built-in sorting functions or libraries. The function should have a time complexity of O(n log n) or better.
"""

def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    
    mid = len(numbers) // 2
    left_half = numbers[:mid]
    right_half = numbers[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
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