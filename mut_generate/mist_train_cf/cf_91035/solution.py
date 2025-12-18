"""
QUESTION:
Write a function `max_sum_submatrix(matrix)` that takes a 2D list of integers as input and returns the maximum sum of a submatrix within the given matrix. The function should handle matrices of any size, and the submatrix can be of any shape. The function should return a single integer representing the maximum sum.
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