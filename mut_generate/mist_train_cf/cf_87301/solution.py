"""
QUESTION:
Implement an efficient stable sorting algorithm in Python that sorts a list of integers in ascending order. The algorithm should have a time complexity of O(n log n) and should not use the built-in sort() function or any other pre-existing sorting function. Additionally, implement a function called 'check_sorted' that takes in a list of integers and returns True if the list is sorted in ascending order, and False otherwise, with a time complexity of O(n).
"""

def entrance(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = entrance(left_half)
    right_half = entrance(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

def check_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True