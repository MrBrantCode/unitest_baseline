"""
QUESTION:
Implement a function named `sort_array` that sorts an input array in ascending order using the bubble sort algorithm. The function should take an array `arr` as input and return the sorted array. The function should compare adjacent elements in the array and swap them if they are in the wrong order. The process should be repeated until the array is fully sorted.
"""

def sort_array(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr