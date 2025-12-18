"""
QUESTION:
Implement a function `search(matrix, target)` that uses binary search to find a given element (`target`) in a sorted 2D matrix (`matrix`). The matrix has the properties that integers in each row are sorted from left to right and the first integer of each row is greater than the last integer of the previous row. The function should return `True` if the target is found, and `False` otherwise. The solution should achieve a time complexity of O(log(n)), where n is the total number of elements in the matrix.
"""

def search(matrix, target):
    if not matrix:
        return False

    rows, columns = len(matrix), len(matrix[0])
    low, high = 0, rows * columns

    while low < high:
        mid = (low + high) // 2
        if matrix[mid // columns][mid % columns] < target:
            low = mid + 1
        else:
            high = mid

    return low < rows * columns and matrix[low // columns][low % columns] == target