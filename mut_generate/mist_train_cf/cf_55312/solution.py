"""
QUESTION:
Implement a function called `quick_sort(arr)` that sorts an input array `arr` containing elements of either integer or string type in ascending order using the quick sort algorithm. The function should handle arrays of varying lengths, including those with fewer than two elements, without errors.
"""

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)