"""
QUESTION:
Implement a function `TwoDTernarySearch(matrix, target)` that performs a ternary search on a two-dimensional list of integers to find a target integer. The matrix is sorted in ascending order by rows and columns. The function should return the path it takes to find the target integer as a list of (row, column) pairs. If the target is not found, return "Target Not Found".
"""

def TernarySearchOnColumns(matrix, row, target, start, end, path):
    if start <= end:
        mid1 = start + (end-start)//3
        mid2 = end - (end-start)//3

        path.append((row, mid1))
        if matrix[row][mid1] == target:
            return path

        path.append((row, mid2))
        if matrix[row][mid2] == target:
            return path

        if target < matrix[row][mid1]:
            return TernarySearchOnColumns(matrix, row, target, start, mid1-1, path)
        elif target > matrix[row][mid2]:
            return TernarySearchOnColumns(matrix, row, target, mid2+1, end, path)
        else:
            return TernarySearchOnColumns(matrix, row, target, mid1+1, mid2-1, path)

    return False

def TernarySearchOnRows(matrix, target, start, end, path):
    if start <= end:
        mid1 = start + (end-start)//3
        mid2 = end - (end-start)//3

        path.append((mid1, -1))
        path.append((mid2, -1))
        if matrix[mid1][0] <= target <= matrix[mid1][-1]:
            return TernarySearchOnColumns(matrix, mid1, target, 0, len(matrix[mid1])-1, path)
        elif matrix[mid2][0] <= target <= matrix[mid2][-1]:
            return TernarySearchOnColumns(matrix, mid2, target, 0, len(matrix[mid2])-1, path)
        elif target < matrix[mid1][0]:
            return TernarySearchOnRows(matrix, target, start, mid1-1, path)
        elif target > matrix[mid2][-1]:
            return TernarySearchOnRows(matrix, target, mid2+1, end, path)
        else:
            return TernarySearchOnRows(matrix, target, mid1+1, mid2-1, path)

    return False

def TwoDTernarySearch(matrix, target):
    path = []
    result = TernarySearchOnRows(matrix, target, 0, len(matrix)-1, path)
    return result if result else "Target Not Found"