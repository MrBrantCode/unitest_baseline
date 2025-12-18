"""
QUESTION:
Find the k-th largest value in a numeric array using recursion. The array may contain negative numbers and will always have at least k elements, where k is a positive integer. The solution should have a time complexity of O(n log k), where n is the size of the array, and should be able to handle large arrays. Implement a function named `find_kth_largest` that takes an array `arr` and an integer `k` as inputs.
"""

def findKthLargest(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = arr[0]
    smaller = [x for x in arr[1:] if x <= pivot]
    larger = [x for x in arr[1:] if x > pivot]
    
    if k == len(larger) + 1:
        return pivot
    elif k <= len(larger):
        return findKthLargest(larger, k)
    else:
        return findKthLargest(smaller, k - len(larger) - 1)