"""
QUESTION:
Implement the function `bubble_sort(arr)` that sorts a list of integers in ascending order using the Bubble Sort algorithm with a time complexity of O(n^2). The input list contains up to 1,000,000 integers ranging from -10,000,000 to 10,000,000, and may include duplicate integers and negative integers. The function should not use any built-in sorting functions or data structures.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr