"""
QUESTION:
Implement a function named 'selection_sort' that takes an array of integers as input and sorts it in ascending order using the selection sort technique. The time complexity should be less than O(n^2) and the space complexity should be less than O(n). The function should be able to handle arrays containing duplicate integers without sacrificing the time and space complexity requirements.
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] == arr[min_index] and j != min_index:
                continue  # Skip duplicate elements
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr