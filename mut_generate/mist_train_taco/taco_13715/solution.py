"""
QUESTION:
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:


       Integers in each row are sorted in ascending from left to right.
       Integers in each column are sorted in ascending from top to bottom.


Example:

Consider the following matrix:


[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]


Given target = 5, return true.

Given target = 20, return false.
"""

def search_sorted_matrix(matrix, target):
    """
    Searches for a target value in a given m x n matrix where:
    - Integers in each row are sorted in ascending order from left to right.
    - Integers in each column are sorted in ascending order from top to bottom.

    Parameters:
    - matrix (List[List[int]]): A 2D list of integers.
    - target (int): The value to search for in the matrix.

    Returns:
    - bool: True if the target is found in the matrix, False otherwise.
    """
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])
    if n == 0:
        return False
    
    row, col = 0, n - 1
    while row < m and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    
    return False