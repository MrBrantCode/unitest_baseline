"""
QUESTION:
Write a function `binary_search_matrix` to perform a recursive binary search in a sorted matrix. The matrix is sorted in increasing order from left to right for each row and from top to bottom for each column. The function should find a target number in the matrix and return True if found, False otherwise. The function should have a time complexity of O(log(m*n)) where 'm' is the number of rows and 'n' is the number of columns in the matrix.
"""

def binary_search_matrix(matrix, target):
    if not matrix:
        return False
    r_len, c_len = len(matrix), len(matrix[0])
    left, right = 0, r_len * c_len - 1

    while left <= right:
        mid = left + (right - left)//2
        temp_r, temp_c = divmod(mid, c_len)
        num = matrix[temp_r][temp_c]

        if num == target:
            return True
        elif num < target:
            left = mid + 1
        else:
            right = mid - 1
    return False