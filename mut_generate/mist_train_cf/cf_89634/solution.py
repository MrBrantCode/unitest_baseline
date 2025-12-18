"""
QUESTION:
Implement the `bubble_sort` function to sort an array in ascending order using the Bubble Sort algorithm. The function should have a time complexity of O(n^2) and a space complexity of O(1), where n is the number of elements in the array. The function should take one argument, `arr`, which is the input array to be sorted. The function should return the sorted array.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swaps = False
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps = True
        if not swaps:
            break
    return arr