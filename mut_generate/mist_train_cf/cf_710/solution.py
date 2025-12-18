"""
QUESTION:
Implement a function `quicksort(arr)` that sorts the input array using the quicksort algorithm. The function should handle duplicate elements in the input array and have a time complexity of O(nlogn). Additionally, include error handling for scenarios where the input array is empty or contains only one element.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)