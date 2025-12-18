"""
QUESTION:
Find a peak element in a 2D matrix, which is an element that is strictly greater than its four neighbors (up, down, left, and right). Given a 2D integer matrix `matrix`, return the index of any peak element.

Constraints:
- 1 ≤ matrix length and each row length ≤ 1000
- -2^31 ≤ matrix elements ≤ 2^31 - 1
- All adjacent elements are distinct
"""

def findPeakGrid(mat):
    m, n = len(mat), len(mat[0])
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2
        max_row = max(range(m), key = lambda i: mat[i][mid])

        if (mid == 0 or mat[max_row][mid] > mat[max_row][mid - 1]) and (mid == n - 1 or mat[max_row][mid] > mat[max_row][mid + 1]):
            return [max_row, mid]
        elif mid > 0 and mat[max_row][mid] < mat[max_row][mid - 1]:
            high = mid - 1
        else:
            low = mid + 1