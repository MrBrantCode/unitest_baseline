"""
QUESTION:
Implement the Quick Sort algorithm in a function named `quick_sort` or `quick_sort_modified` that can efficiently handle a list of numbers ranging from -1000 to 1000, including duplicates, with up to 1 million elements. If the input list is already sorted in ascending order, use the middle element as the pivot instead of the first element.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    elif arr == sorted(arr):
        middle = len(arr) // 2
        pivot = arr[middle]
        less = [x for x in arr[:middle] if x <= pivot] + [x for x in arr[middle+1:] if x <= pivot]
        greater = [x for x in arr[:middle] if x > pivot] + [x for x in arr[middle+1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)