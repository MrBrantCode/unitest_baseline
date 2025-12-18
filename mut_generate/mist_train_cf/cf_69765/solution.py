"""
QUESTION:
Write a function `min_path_sum(matrix)` that takes a 2D list of integers as input, representing an n x m matrix, and returns the minimum sum of the path from the upper left to the lower right, with the constraint of only moving right or down. The function should have a time complexity of O(n*m) and a space complexity of O(n*m).
"""

def min_path_sum(matrix):
    """
    This function calculates the minimum sum of the path from the upper left to the lower right
    of a given matrix, with the constraint of only moving right or down.

    Args:
        matrix (list): A 2D list of integers representing an n x m matrix.

    Returns:
        int: The minimum sum of the path from the upper left to the lower right of the matrix.
    """
    
    height = len(matrix)
    width = len(matrix[0])

    PathCost = [[0 for x in range(width+1)] for y in range(height+1)] 

    # Initialize the base case
    for i in range(1, width+1):
        PathCost[0][i] = float("inf")

    for i in range(1, height+1):
        PathCost[i][0] = float("inf")

    PathCost[1][1] = matrix[0][0]

    # Build rest of the path cost matrix 
    for i in range(1, height+1):
        for j in range(1, width+1):
            if i==1 and j==1:
                continue
            PathCost[i][j] = min(PathCost[i-1][j], PathCost[i][j-1]) + matrix[i-1][j-1]
            
    # The minimum path sum is stored at the bottom-right corner of the PathCost
    return PathCost[height][width]