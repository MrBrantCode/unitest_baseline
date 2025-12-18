"""
QUESTION:
Given a row-sorted binary matrix `binaryMatrix`, return the index (0-indexed) of the leftmost column with a 1 in it and the total number of 1's in this column. If such a column does not exist, return `-1`. 

The matrix can only be accessed through the `BinaryMatrix` interface: `BinaryMatrix.get(row, col)` returns the element at `(row, col)`, and `BinaryMatrix.dimensions()` returns the dimensions of the matrix as `[rows, cols]`. The solution must not make more than 1000 calls to `BinaryMatrix.get`.
"""

def entance(binaryMatrix):
    rows, cols = binaryMatrix.dimensions()
    current_col = cols
    total_ones = 0
    
    # Run binary search on each row.
    for row in range(rows):
        left, right = 0, current_col
        while left < right:
            mid = (left + right) // 2
            if binaryMatrix.get(row, mid) == 1:
                right = mid
            else:
                left = mid + 1
        current_col = left
        total_ones += binaryMatrix.get(row, current_col)
    
    if current_col == cols:
        return -1
    else:
        return [current_col, total_ones]