"""
QUESTION:
Write a function `find_kth_largest(arr, k)` to find the k-th largest value in a numeric array using recursion, where k is a positive integer and the array has at least k elements. The function should have a time complexity of O(n log k), where n is the size of the array.
"""

def find_kth_largest(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = arr[0]
    smaller = [x for x in arr[1:] if x <= pivot]
    larger = [x for x in arr[1:] if x > pivot]
    
    if k == len(larger) + 1:
        return pivot
    elif k <= len(larger):
        return find_kth_largest(larger, k)
    else:
        return find_kth_largest(smaller, k - len(larger) - 1)