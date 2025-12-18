"""
QUESTION:
Develop a function `find_target(matrix, target)` that traverses a 2D matrix in a right-down direction (only moving right or down) and returns a tuple containing the index of the first occurrence of the target value and the total number of steps taken to reach the target, where steps are counted from the top-left corner (0,0). The index is zero-based. If the target is not found, the function should return `None`.
"""

def entrance(matrix, target):
    steps = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            steps += 1
            if matrix[i][j] == target:
                return ((i, j), steps)