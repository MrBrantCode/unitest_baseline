"""
QUESTION:
Implement a function `quick_sort(arr)` that sorts an array of integers using the Quick Sort algorithm with a guaranteed time complexity of O(nlogn) in all cases.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Selecting the pivot element
    less_than = [x for x in arr if x < pivot]  # Elements less than the pivot
    equal_to = [x for x in arr if x == pivot]  # Elements equal to the pivot
    greater_than = [x for x in arr if x > pivot]  # Elements greater than the pivot
    return quick_sort(less_than) + equal_to + quick_sort(greater_than)  # Combining the sorted sub-arrays