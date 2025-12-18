"""
QUESTION:
Implement a function named `quicksort` that sorts an array of elements in ascending order. The function should be able to handle duplicate elements and have a time complexity of O(nlogn), where n is the number of elements in the input array.
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quicksort(less) + equal + quicksort(greater)