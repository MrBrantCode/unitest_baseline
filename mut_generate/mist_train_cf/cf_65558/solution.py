"""
QUESTION:
Write a function named `findPath` that takes a 2D matrix and its dimensions as input, and prints all possible paths from the top-left cell to the bottom-right cell. The function should use a Depth-First Search algorithm, moving only down or right at each step. The path should be represented as a string of 'D' (down) and 'R' (right). The function should not take into account the actual values in the matrix, only its dimensions.
"""

def findPath(matrix, n, m):
    """
    This function prints all possible paths from the top-left cell to the bottom-right cell in a 2D matrix.
    
    Args:
    matrix (list): A 2D matrix (not used in the function)
    n (int): The number of rows in the matrix
    m (int): The number of columns in the matrix
    """
    
    def dfs(position, path):
        # If we reach the bottom-right corner
        if position == (n-1, m-1):
            print(path)
            return

        # We move right
        if 0 <= position[1] + 1 < m:
            position_new = (position[0], position[1] + 1)
            dfs(position_new, path + 'R')
        
        # We move down
        if 0 <= position[0] + 1 < n:
            position_new = (position[0] + 1, position[1])
            dfs(position_new, path + 'D')

    # Start the DFS traversal from the top-left corner
    dfs((0, 0), '')