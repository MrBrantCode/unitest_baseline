"""
QUESTION:
Create a function `compare_arrays_modulo` that compares two input arrays while ignoring any duplicate elements, maintaining the order of the remaining elements, and only considering the elements that are multiples of a given number (3 in this case). The function should return a boolean indicating whether the two arrays are equal after applying the specified conditions.
"""

def compare_arrays_modulo(arr1, arr2):
    # Remove duplicate elements while maintaining order
    arr1 = list(dict.fromkeys(arr1))
    arr2 = list(dict.fromkeys(arr2))

    # Filter out elements that are not multiples of 3
    arr1_filtered = [num for num in arr1 if num % 3 == 0]
    arr2_filtered = [num for num in arr2 if num % 3 == 0]

    # Compare the filtered arrays
    return arr1_filtered == arr2_filtered