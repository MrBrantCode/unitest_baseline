"""
QUESTION:
Create a function named `combine_arrays` that takes two arrays of numbers (`arr1` and `arr2`) as input. The function should merge the two arrays, remove duplicate elements, sort the resulting array in ascending order, and return the sorted array in descending order. The function should handle arrays with duplicate elements, empty arrays, and arrays containing negative numbers.
"""

def combine_arrays(arr1, arr2):
    # Combine the two arrays
    combined_array = arr1 + arr2

    # Remove duplicate elements
    combined_array = list(set(combined_array))

    # Sort the array in ascending order
    combined_array.sort()

    # Return the result in descending order
    return sorted(combined_array, reverse=True)