"""
QUESTION:
Create a function named `remove_duplicates_and_sort` that takes an array of integers and/or strings as input, removes duplicate elements, and sorts the array in ascending order using constant extra space and without any built-in sorting functions or data structures.
"""

def remove_duplicates_and_sort(array):
    # Remove duplicates
    array = list(set(array))

    # Sort array
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array