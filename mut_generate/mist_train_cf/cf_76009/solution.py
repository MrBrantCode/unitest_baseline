"""
QUESTION:
Write a function named `process_array` that takes a 2D array as input, where each sub-array is of size N (N <= 10), and returns a 1D array of unique numbers in descending order. The input array may contain duplicate numbers, and the function should remove these duplicates before sorting.
"""

def process_array(arr):
    # Flatten the 2D array and remove duplicates using set
    unique_nums = set(num for sublist in arr for num in sublist)

    # Sort the unique numbers in descending order and return the result
    return sorted(unique_nums, reverse=True)