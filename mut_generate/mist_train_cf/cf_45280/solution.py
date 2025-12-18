"""
QUESTION:
Create a function called `sort_descending` that takes an array of numbers as input and returns the sorted array in descending order. The function should not use built-in sorting functions and should handle arrays containing negative numbers and duplicate elements.
"""

def sort_descending(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr