"""
QUESTION:
Create a function named `arrange_checker` that takes a list of integers as input and returns a tuple containing the smallest index of an element which is larger than the element immediately following it and the input list in ascending order. If no such element exists, return -1 along with the original list unchanged. The input list will not contain any repeated values and the function should not utilize any built-in sorting functions.
"""

def arrange_checker(arr):
    idx = -1
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                if idx == -1:
                    idx = j
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return (idx, arr)