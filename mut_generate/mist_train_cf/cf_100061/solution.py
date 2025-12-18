"""
QUESTION:
Implement the `quicksort` function to sort an array of integers in ascending order. The input array can have arbitrary length and is not pre-sorted. The function should have a time complexity of O(nlogn) and should be able to handle large datasets.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)