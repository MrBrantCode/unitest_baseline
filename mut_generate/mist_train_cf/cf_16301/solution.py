"""
QUESTION:
Implement a function named `quick_sort_modified` that sorts a list of integers using the Quick Sort algorithm. The list can contain up to 1 million elements, including duplicates and negative numbers in the range of -1000 to 1000. If the list is already sorted in ascending order, use the middle element as the pivot; otherwise, use the first element as the pivot. The function should return the sorted list.
"""

def quick_sort_modified(arr):
    if len(arr) <= 1:
        return arr
    elif arr == sorted(arr):
        middle = len(arr) // 2
        pivot = arr[middle]
        less = [x for x in arr[:middle] if x <= pivot] + [x for x in arr[middle+1:] if x <= pivot]
        greater = [x for x in arr[:middle] if x > pivot] + [x for x in arr[middle+1:] if x > pivot]
        return quick_sort_modified(less) + [pivot] + quick_sort_modified(greater)
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort_modified(less) + [pivot] + quick_sort_modified(greater)