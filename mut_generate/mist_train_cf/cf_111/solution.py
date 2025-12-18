"""
QUESTION:
Write a function `bubble_sort(arr)` that sorts an array of integers in ascending order, allowing for duplicate elements, and has a time complexity of O(n^2).
"""

def entrance(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr