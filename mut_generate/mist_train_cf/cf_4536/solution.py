"""
QUESTION:
Write a function called `transpose_array` that takes a 2D array of integers as input, checks if it is a square matrix, and returns its transpose. The function should validate that each element in the array is within the range of -10^9 to 10^9 and raise an exception if any element is outside this range or if the input array is not a square matrix.
"""

def transpose_array(arr):
    # Check if the array is a square matrix
    n = len(arr)
    if any(len(row) != n for row in arr):
        raise Exception("Input array is not a square matrix")

    # Check if all elements are within the valid range
    for row in arr:
        for element in row:
            if not (-10**9 <= element <= 10**9):
                raise Exception("Input array contains elements outside the valid range")

    # Transpose the array
    transposed = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transposed[j][i] = arr[i][j]

    return transposed