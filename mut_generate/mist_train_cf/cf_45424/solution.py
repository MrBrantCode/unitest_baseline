"""
QUESTION:
Write a function named `bubbleSort` that takes a list of decimal numbers as input and returns a new list with the same numbers in ascending order. The function should handle lists containing negative decimals and multiple entries of the same decimal. If the input list is empty, the function should return an empty list. Implement the function to accept user input as a comma-separated string of decimals and raise a user-friendly error message if the input is not a valid decimal number.
"""

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr