"""
QUESTION:
Implement a function named `max_submatrix` that takes a two-dimensional matrix of integers as input and returns the maximum possible cumulative sum of elements in any submatrix. The function should be able to handle a matrix of any size and content.
"""

def max_submatrix(matrix):
    def max_subarray_sum(arr):
        cur_sum = max_sum = arr[0]
        for num in arr[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(cur_sum, max_sum)
        return max_sum

    max_sum = -float('inf')
    rows = len(matrix)
    cols = len(matrix[0])

    for left in range(cols):
        temp = [0]*rows
        for right in range(left, cols):
            for i in range(rows):
                temp[i] += matrix[i][right]

            cur_sum = max_subarray_sum(temp)
            max_sum = max(cur_sum, max_sum)

    return max_sum