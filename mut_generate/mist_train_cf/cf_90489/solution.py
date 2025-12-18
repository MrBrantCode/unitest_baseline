"""
QUESTION:
Given a 2D matrix of integers, implement the function `max_sum_submatrix(matrix)` that retrieves the maximum sum submatrix with a size of at least 2 x 2. The matrix may contain negative integers. If the matrix is empty, return 0 as the maximum sum. If multiple submatrices have the same maximum sum, return any one of them. The algorithm should have a time complexity of O(n^3), where n is the size of the matrix, and a space complexity of O(n^2).
"""

def max_sum_submatrix(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float('-inf')
    left = right = top = bottom = 0

    for l in range(cols):
        sums = [0] * rows

        for r in range(l, cols):
            for i in range(rows):
                sums[i] += matrix[i][r]

            current_sum = 0
            current_top = 0

            for i in range(rows):
                if current_sum < 0:
                    current_sum = sums[i]
                    current_top = i
                else:
                    current_sum += sums[i]

                if current_sum > max_sum:
                    max_sum = current_sum
                    left = l
                    right = r
                    top = current_top
                    bottom = i

    return max_sum