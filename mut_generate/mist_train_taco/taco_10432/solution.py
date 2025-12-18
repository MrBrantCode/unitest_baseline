"""
QUESTION:
<image>

Input

The input contains two integers row, col (0 ≤ row, col ≤ 63), separated by a single space.

Output

Output "IN" or "OUT".

Examples

Input


0 0


Output


OUT


Input


27 0


Output


IN


Input


0 27


Output


OUT


Input


27 27


Output


IN
"""

def check_circle_position(row, col, circle_patterns):
    """
    Checks if a given position is inside or outside a circle defined by a set of binary patterns.

    Args:
        row (int): The row number of the position to check (0 ≤ row ≤ 63)
        col (int): The column number of the position to check (0 ≤ col ≤ 63)
        circle_patterns (list): A 2D list of binary strings representing the circle patterns

    Returns:
        str: 'IN' if the position is inside the circle, 'OUT' otherwise
    """
    if row < 0 or row >= len(circle_patterns) or col < 0 or col >= len(circle_patterns[0]):
        return 'OUT'
    return 'IN' if circle_patterns[row][col] == '1' else 'OUT'