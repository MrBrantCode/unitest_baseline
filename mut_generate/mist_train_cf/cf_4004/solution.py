"""
QUESTION:
Implement a function called `bubble_sort_optimized` that sorts a given list of integers in ascending order. The function should optimize the Bubble Sort algorithm by introducing a flag variable to track if any swaps occurred during each pass, allowing it to break out of the loop when the list is already sorted. The function should have a time complexity of O(n) in the best-case scenario and a space complexity of O(1). The input list can contain duplicate elements, and the function should preserve their relative order.
"""

def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr