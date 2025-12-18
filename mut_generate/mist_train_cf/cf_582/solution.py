"""
QUESTION:
Write a function named `combine_arrays` that takes two arrays `arr1` and `arr2` as input, combines them into a single array, removes any duplicate elements, sorts the array in ascending order, and returns the result in descending order. The function should be able to handle arrays with duplicate elements, empty arrays, and arrays with negative numbers.
"""

def entance(arr1, arr2):
    combined_array = arr1 + arr2
    combined_array = list(set(combined_array))
    combined_array.sort()
    return sorted(combined_array, reverse=True)