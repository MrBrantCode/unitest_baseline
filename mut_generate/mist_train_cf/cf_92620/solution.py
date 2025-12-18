"""
QUESTION:
Implement a function named `quicksort_descending` that sorts an array of integers in descending order without using any built-in sorting functions or libraries. The time complexity of the implementation should be less than O(n^2) and the space complexity should be less than O(n). The function should take an array of integers as input and return the sorted array.
"""

def quicksort_descending(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    larger = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]
    smaller = [x for x in arr if x < pivot]
    
    return quicksort_descending(larger) + equal + quicksort_descending(smaller)