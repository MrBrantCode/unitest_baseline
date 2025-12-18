"""
QUESTION:
Implement the `pack_canvas` function, which takes a 2D list `canvas` and a list of tuples `objects` as input. The `canvas` represents a rectangular grid of cells where 0 denotes an empty cell and 1 denotes an occupied cell. Each tuple in `objects` represents a rectangular object with its top-left corner coordinates and width and height.

The function should attempt to place each object on the canvas without overlapping with other objects or extending beyond the canvas boundaries. If a valid position is found, update the canvas by setting the corresponding cells to 1. If not, leave the canvas unchanged. The function should return the updated canvas after attempting to place all objects.

The `canvas` and `objects` parameters should be modified as follows:
- `canvas`: a 2D list of integers with 0 representing empty cells and 1 representing occupied cells.
- `objects`: a list of tuples, where each tuple contains the top-left corner coordinates (x, y) and the width and height of a rectangular object.
"""

def pack_canvas(canvas, objects):
    def is_valid_position(x, y, width, height):
        for i in range(x, x + width):
            for j in range(y, y + height):
                if i < 0 or i >= len(canvas) or j < 0 or j >= len(canvas[0]) or canvas[i][j] == 1:
                    return False
        return True

    def place_object(x, y, width, height):
        for i in range(x, x + width):
            for j in range(y, y + height):
                canvas[i][j] = 1

    for obj in objects:
        x, y, width, height = obj
        if is_valid_position(x, y, width, height):
            place_object(x, y, width, height)

    return canvas