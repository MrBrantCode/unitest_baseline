"""
QUESTION:
Write a function called `traverse_spiral` that traverses a two-dimensional array in a spiral pattern, starting from the top left corner and moving clockwise until reaching the center of the array. The function should calculate the sum of all the elements traversed and find the maximum and minimum values encountered during the traversal. The array size can be up to 1,000,000 x 1,000,000 and the function must complete the traversal in less than 1 second. The array can contain positive or negative integers between -1,000,000 and 1,000,000 inclusive.
"""

def traverse_spiral(matrix):
    if not matrix or not matrix[0]:
        return 0, float('inf'), float('-inf')

    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    dir_index = 0
    row, col = 0, 0
    total_sum = 0
    min_val = float('inf')
    max_val = float('-inf')

    for _ in range(rows * cols):
        total_sum += matrix[row][col]
        min_val = min(min_val, matrix[row][col])
        max_val = max(max_val, matrix[row][col])
        visited[row][col] = True

        next_row, next_col = row + directions[dir_index][0], col + directions[dir_index][1]
        if 0 <= next_row < rows and 0 <= next_col < cols and not visited[next_row][next_col]:
            row, col = next_row, next_col
        else:
            dir_index = (dir_index + 1) % 4
            row, col = row + directions[dir_index][0], col + directions[dir_index][1]

    return total_sum, min_val, max_val