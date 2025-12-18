"""
QUESTION:
Write a function called `check_constraint` that takes in three parameters: `cell_to_uncover`, `board`, and `radius`, where `radius` defaults to 2. The function should return `True` if no cells within the specified `radius` of `cell_to_uncover` on the `board` have more than three potential mines, and `False` otherwise. The `board` is a 10x10 grid, where each cell is represented by a number indicating the number of potential mines. The `cell_to_uncover` is a tuple of two integers representing the coordinates of the cell to uncover.
"""

def check_constraint(cell_to_uncover, board, radius=2):
    """
    Check if any cells within the specified radius of cell_to_uncover on the board have more than three potential mines.

    Args:
    cell_to_uncover (tuple): A tuple of two integers representing the coordinates of the cell to uncover.
    board (list): A 10x10 grid, where each cell is represented by a number indicating the number of potential mines.
    radius (int, optional): The radius to check. Defaults to 2.

    Returns:
    bool: True if no cells within the specified radius have more than three potential mines, False otherwise.
    """

    x, y = cell_to_uncover
    for i in range(max(0, x - radius), min(10, x + radius + 1)):
        for j in range(max(0, y - radius), min(10, y + radius + 1)):
            if (i, j) != cell_to_uncover and board[i][j] > 3:
                return False
    return True