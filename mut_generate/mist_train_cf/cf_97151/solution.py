"""
QUESTION:
Implement a function called `bubble_sort` that sorts an array in descending order using the bubble sort algorithm. The input array will always contain 10^5 elements.
"""

def entance(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
    return arr