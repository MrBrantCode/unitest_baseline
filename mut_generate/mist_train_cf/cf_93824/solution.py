"""
QUESTION:
Implement a function named `insertion_sort` that takes an array of integers as input, sorts the array in descending order using the insertion sort algorithm, and returns the sorted array. The original array should remain unchanged, and the function should not use any built-in sorting functions or libraries. The array can contain up to 100,000 elements, including duplicates.
"""

def insertionsort(arr):
    # create a copy of the original array to leave it unchanged
    arr_copy = arr[:]
    # iterate over each element in the array starting from the second element
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        # compare the key element with each element before it and move them to the right if they are smaller
        while j >= 0 and key > arr_copy[j]:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = key
    return arr_copy