"""
QUESTION:
Implement a function named `sort_array` that sorts an array of integers in ascending order. The function should take a list of integers as input and return the sorted list. The function must use the bubble sort algorithm.
"""

def sort_array(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr