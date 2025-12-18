"""
QUESTION:
Write a function `bubble_sort` that sorts a list of elements in ascending order using the bubble sort algorithm. The function should have a time complexity of O(n^2) in the worst-case scenario and a space complexity of O(1).
"""

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr