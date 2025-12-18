"""
QUESTION:
Implement a function named `sort_array` that takes a list of integers as input and returns a new list with the integers sorted in descending order.
"""

def sort_array(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr