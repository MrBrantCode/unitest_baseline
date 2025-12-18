"""
QUESTION:
Implement the quicksort function that takes an array as input and returns the sorted array in ascending order. The function should handle edge cases such as an empty array or an array with only one element. The time complexity should be O(n log n) in the average and best cases, and the space complexity should be O(n).
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)