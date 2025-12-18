"""
QUESTION:
Create a function named `check_sorted` that takes an array of unique positive integers as input, with a length of at least 2. The function should return a tuple where the first element is a boolean indicating whether the array is sorted in ascending order, and the second element is the index of the first element that violates the sorting order if the array is not sorted, or -1 if the array is sorted. The function should not modify the input array or use any built-in sorting functions.
"""

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False, i+1
    return True, -1