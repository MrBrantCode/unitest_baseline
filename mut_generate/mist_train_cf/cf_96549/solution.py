"""
QUESTION:
Implement a function called `selection_sort` that sorts an array in ascending order using the selection sort algorithm. The input to this function is an array of integers, and the output is the sorted array. The function should have a time complexity of O(n^2).
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
    return arr