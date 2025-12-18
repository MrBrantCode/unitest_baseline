"""
QUESTION:
Write a function named `bubble_sort_descending` that sorts an array of integers in descending order using the bubble sort technique. The array can contain up to 10^6 elements. The solution should have a time complexity of O(n^2) and a space complexity of O(1). The function should take an array as input and return the sorted array in descending order.
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