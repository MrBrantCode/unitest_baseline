"""
QUESTION:
Implement a function `quicksort(arr)` that sorts an input array in ascending order using the quicksort algorithm. The function should handle duplicate values correctly and have an average-case time complexity of O(n log n).
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser = [num for num in arr if num < pivot]
    equal = [num for num in arr if num == pivot]
    greater = [num for num in arr if num > pivot]
    return quicksort(lesser) + equal + quicksort(greater)