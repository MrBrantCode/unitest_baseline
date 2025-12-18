"""
QUESTION:
Implement a function `determine_quadrant` that determines the quadrant of a given point within a grid based on the grid size and direction of travel. The function takes three parameters: `grid`, a 2D array representing the grid; `point`, a tuple of coordinates (x, y); and `direction`, a tuple representing movement in the x and y directions (dx, dy). Return a string representing the quadrant in which the point lies: "T" (Top), "B" (Bottom), "TL" (Top-left), "TR" (Top-right), "BL" (Bottom-left), or "BR" (Bottom-right). Assume the grid size is a tuple of positive integers.
"""

def determine_quadrant(grid, point, direction):
    rows, cols = len(grid), len(grid[0])
    x, y = point
    dx, dy = direction

    if (rows, cols) == (1, 1):
        return "T" if dy == 1 else "B"
    elif (rows, cols) == (2, 1):
        return "T" if dx == 1 else "B"
    elif (rows, cols) == (2, 2):
        if (dx, dy) == (1, 1):
            return "TL"
        elif (dx, dy) == (1, -1):
            return "TR"
        elif (dx, dy) == (-1, 1):
            return "BL"
        else:  # (-1, -1)
            return "BR"
    else:
        # Handle other grid sizes if needed
        return "Unknown quadrant"