"""
QUESTION:
Implement the `quick_sort` function to sort a given array using the Quick Sort algorithm. The function should take one argument `arr`, a list of elements that needs to be sorted. The Quick Sort algorithm should have an average time complexity of O(n log n). The function should return the sorted array.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)