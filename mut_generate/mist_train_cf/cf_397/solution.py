"""
QUESTION:
Implement a function called bubble_sort_descending that sorts a list of integers in descending order. The function should have a time complexity of O(n^2) and use constant space complexity, not utilizing any extra data structures, recursive calls, or built-in sorting functions/libraries. The algorithm must be stable, preserving the relative order of equal elements in the sorted list.
"""

def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr