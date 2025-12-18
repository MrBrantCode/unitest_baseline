"""
QUESTION:
Write a function `spiral_traverse(arr)` that takes a 2D matrix as input and returns a list of elements in spiral order. The spiral order starts from the top left corner and goes clockwise. The input matrix is a list of lists where each inner list has the same length. The function should return a list of elements in the spiral order without modifying the original matrix.
"""

def spiral_traverse(arr):
    res = []
    top_row, bottom_row = 0, len(arr) - 1
    left_col, right_col = 0, len(arr[0]) - 1

    while top_row <= bottom_row and left_col <= right_col:
        for i in range(left_col, right_col + 1):
            res.append(arr[top_row][i])
        top_row += 1

        for i in range(top_row, bottom_row + 1):
            res.append(arr[i][right_col])
        right_col -= 1

        if top_row <= bottom_row:
            for i in range(right_col, left_col - 1, -1):
                res.append(arr[bottom_row][i])
            bottom_row -= 1

        if left_col <= right_col:
            for i in range(bottom_row, top_row - 1, -1):
                res.append(arr[i][left_col])
            left_col += 1

    return res