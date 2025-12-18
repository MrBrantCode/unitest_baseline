"""
QUESTION:
Write a function `maximum_subarray_sum(matrix)` that takes a 2D matrix of integers as input and returns the maximum cumulative sum of any submatrix within it. The function should be able to handle matrices of any size. The submatrix can be of any size and can start and end at any position within the given matrix.
"""

def maximum_subarray_sum(matrix):
    max_sum = float('-inf')
    row_len, col_len = len(matrix), len(matrix[0])

    # Function to find maximum sum of subarray in a 1D array using Kadane's algorithm
    def max_sub_arr_sum(arr):
        max_sum = arr[0]
        max_end = arr[0]
        for i in range(1, len(arr)):
            max_end = max(arr[i], max_end + arr[i])
            max_sum = max(max_sum, max_end)
        return max_sum

    # Iterating through all possible submatrices
    for left in range(col_len):   
        temp = [0 for _ in range(row_len)]  

        for right in range(left, col_len):
            # Updating temp array (To find max in the current right column)
            for i in range(row_len):
                temp[i] += matrix[i][right]

            current_sum = max_sub_arr_sum(temp)
            max_sum = max(max_sum, current_sum)
    return max_sum