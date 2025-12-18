"""
QUESTION:
Write a function called `sortArray` that sorts an array of numbers in ascending order using a selection sort algorithm. The function should take an array of numbers as input, sort it in-place, and return the sorted array. The input array can contain duplicate numbers and may not be empty. The function should have a time complexity of O(n^2), where n is the number of elements in the array.
"""

def sort_array(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr