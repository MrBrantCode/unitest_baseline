"""
QUESTION:
Write a function named `searchMatrix` that takes a sorted two-dimensional matrix `matrix` and a target value `target` as input, and returns `True` if the target is found in the matrix and `False` otherwise. The matrix is sorted in such a way that all elements in a row are sorted in ascending order and the last element of a row is smaller than or equal to the first element of the next row. The function should have a time complexity of O(log(mn)), where m and n are the number of rows and columns in the matrix, respectively.
"""

def searchMatrix(matrix, target):
    def search_rec(left, up, right, down):
        if left > right or up > down:
            return False
        elif target < matrix[up][left] or target > matrix[down][right]:
            return False

        mid = left + (right - left) // 2

        row = up
        while row <= down and matrix[row][mid] <= target:
            if matrix[row][mid] == target:
                return True
            row += 1

        return search_rec(left, row, mid - 1, down) or search_rec(mid + 1, up, right, row - 1)

    return search_rec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)