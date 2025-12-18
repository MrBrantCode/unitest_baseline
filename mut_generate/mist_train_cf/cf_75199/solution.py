"""
QUESTION:
Implement a function named `quick_sort` that sorts an input list of integers in ascending order using the quicksort algorithm. The function should have a time complexity of O(n log n) on average and handle lists of any size.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        less = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quick_sort(less) + middle + quick_sort(greater)