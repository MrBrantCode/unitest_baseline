"""
QUESTION:
Write a function called `transpose_array` that takes a 2D array of maximum 100 rows and 100 columns as input. The function should transpose the array, convert any negative numbers to their absolute values, and remove any duplicate elements from the transposed array. If the input array is empty or contains non-numeric values, the function should return an empty array.
"""

def transpose_array(arr):
    # Check for empty or non-numeric array
    if len(arr) == 0 or any(not isinstance(element, (int, float)) for row in arr for element in row):
        return []

    # Transpose the array
    transposed_arr = [[row[i] for row in arr] for i in range(len(arr[0]))]

    # Convert negative numbers to absolute values and remove duplicates
    transposed_arr = [list(set([abs(element) for element in row])) for row in transposed_arr]

    return transposed_arr