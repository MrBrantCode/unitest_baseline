"""
QUESTION:
Implement a recursive function `cocktail_sort` that takes a list of positive integers and sorts the list elements in ascending order using the cocktail sort algorithm, without using any built-in sorting functions or methods, and with a time complexity of O(n^2). The function should return the sorted list.
"""

def cocktail_sort(arr):
    n = len(arr)
    swapped = False

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            swapped = True

    if not swapped:
        return arr

    swapped = False

    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            swapped = True

    if not swapped:
        return arr

    return cocktail_sort(arr)