"""
QUESTION:
Develop a function `quickSort` that sorts an input list of integers using the QuickSort algorithm. The function should recursively partition the list around a chosen pivot and sort the sublists until each sublist contains only one element. The choice of pivot should be such that it divides the list into two halves of roughly equal size to achieve an average-case time complexity of O(n log n).
"""

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)