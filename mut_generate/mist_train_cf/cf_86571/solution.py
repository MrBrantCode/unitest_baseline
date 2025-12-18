"""
QUESTION:
Implement a function named `quicksort` that sorts an input array using the quicksort algorithm. The function should handle duplicate elements and have a time complexity of O(nlogn). It should also handle edge cases where the input array is empty or contains only one element. The function should return the sorted array.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)