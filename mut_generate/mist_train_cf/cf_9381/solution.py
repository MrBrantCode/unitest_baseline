"""
QUESTION:
Implement a function `quicksort(arr)` that sorts an array in ascending order using the quicksort algorithm. The function should handle duplicate elements and have a time complexity of O(nlogn), where n is the number of elements in the array.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + equal + quicksort(greater)