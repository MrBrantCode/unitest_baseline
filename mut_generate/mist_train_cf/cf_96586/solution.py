"""
QUESTION:
Implement the quicksort function in Python. The function should sort an array of integers in ascending order. The function should handle duplicate values and should not use built-in sort functions. The function should also have a time complexity of O(n log n) on average.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser, equal, greater = [], [], []
    for num in arr:
        if num < pivot:
            lesser.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)
    return quicksort(lesser) + equal + quicksort(greater)