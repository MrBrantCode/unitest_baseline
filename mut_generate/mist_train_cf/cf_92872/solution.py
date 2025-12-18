"""
QUESTION:
Implement the `selection_sort` function to sort an array of integers in ascending order using the selection sort algorithm. The function should take an array of integers as input and return the sorted array. The time complexity of the function should be O(n^2), where n is the number of elements in the array.
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr