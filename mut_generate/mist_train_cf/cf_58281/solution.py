"""
QUESTION:
Implement a function `quick_sort(arr)` to efficiently sort an array of integers, which may include duplicates and negative values, with optimal time and space complexity. The function should handle a significant volume of data and should be able to sort in-place.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)