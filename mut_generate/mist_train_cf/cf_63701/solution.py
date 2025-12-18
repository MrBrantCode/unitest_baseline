"""
QUESTION:
Implement a function `quick_sort(arr)` that sorts a list of integers in ascending order without using any built-in or library sorting functions, achieving an average-case time complexity of at least O(n log n). The function should handle edge cases such as an already sorted array, a reverse sorted array, and an array with all elements the same.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)