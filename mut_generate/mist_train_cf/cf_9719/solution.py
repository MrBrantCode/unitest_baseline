"""
QUESTION:
Write a function named `max_sum_submatrix` that takes a 2D list `matrix` as input and returns the maximum sum of a submatrix within it. The submatrix can be of any size, and the function should handle both positive and negative numbers in the matrix.
"""

def max_sum_submatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    maxSum = float('-inf')

    for left in range(cols):
        temp = [0] * rows
        for right in range(left, cols):
            for i in range(rows):
                temp[i] += matrix[i][right]

            currentSum = 0
            for i in range(rows):
                if currentSum < 0:
                    currentSum = temp[i]
                else:
                    currentSum += temp[i]
                
                if currentSum > maxSum:
                    maxSum = currentSum

    return maxSum