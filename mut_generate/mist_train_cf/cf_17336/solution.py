"""
QUESTION:
Implement a function called `spiral_traverse(matrix)` that takes a 2D list `matrix` as input and returns a list of its elements in spiral order. The function should have a time complexity of O(n*m) and space complexity of O(1), where n and m are the dimensions of the matrix. The dimensions of the matrix are constrained such that 1 ≤ n, m ≤ 10^3, and the elements of the matrix can be integers ranging from -10^3 to 10^3.
"""

def spiral_traverse(matrix):
    result = []
    top_row, bottom_row = 0, len(matrix) - 1
    left_col, right_col = 0, len(matrix[0]) - 1

    while top_row <= bottom_row and left_col <= right_col:
        for col in range(left_col, right_col + 1):
            result.append(matrix[top_row][col])
        top_row += 1

        for row in range(top_row, bottom_row + 1):
            result.append(matrix[row][right_col])
        right_col -= 1

        if top_row <= bottom_row:
            for col in range(right_col, left_col - 1, -1):
                result.append(matrix[bottom_row][col])
            bottom_row -= 1

        if left_col <= right_col:
            for row in range(bottom_row, top_row - 1, -1):
                result.append(matrix[row][left_col])
            left_col += 1

    return result