"""
QUESTION:
Write a function called `transpose_array` that takes a 2D array of maximum 100 rows and 100 columns as input. The function should handle edge cases where the input array is empty or contains non-numeric values, and it should convert any negative numbers to their absolute values before transposing. After transposing, the function should remove any duplicate elements from each row of the transposed array.
"""

def transpose_array(arr):
    # Check for empty or non-numeric array
    if len(arr) == 0 or any(not isinstance(element, (int, float)) for row in arr for element in row):
        return []

    # Transpose the array and convert negative numbers to absolute values
    transposed_arr = [[abs(arr[j][i]) for j in range(len(arr))] for i in range(len(arr[0]))]

    # Remove duplicate elements from the transposed array
    transposed_arr = [list(set(row)) for row in transposed_arr]

    # Return the transposed array
    return transposed_arr