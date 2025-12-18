"""
QUESTION:
Given a matrix with non-ascending or non-descending order across both rows and columns, write a function `find_missing_positive(matrix)` that finds the least positive integer missing from the matrix. The solution should have a computational complexity of O(n^2) and a space complexity of O(1), where n is the number of elements in the matrix. The function should handle edge cases where the matrix contains only negative numbers or zeros, and repeated numbers.
"""

def find_missing_positive(matrix):
    n = len(matrix[0])
    m = len(matrix)

    i = 0
    while i < m and matrix[i][0] <= 0:
        i += 1

    target = 1
    while i < m:
        j = 0
        while j < n and matrix[i][j] < target:
            j += 1

        if j == n or matrix[i][j] > target:
            return target
        else:  # If matrix[i][j] == target
            target += 1
            j += 1
            while j < n and matrix[i][j] == target:
                target += 1
                j += 1

        i += 1

    return target