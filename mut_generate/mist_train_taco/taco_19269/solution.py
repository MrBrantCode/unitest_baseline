"""
QUESTION:
problem

I want to put as many rectangular tiles as possible on a rectangular wall with a size of $ h $ in height and $ w $ in width, and a size of $ a $ in height and $ b $ in width.

The following conditions must be met when attaching tiles.


* Do not stack tiles.
* Do not apply tiles diagonally, that is, any edge of the tile is parallel or perpendicular to any edge of the wall.
* Do not change the orientation of the tiles, that is, do not swap the vertical and horizontal directions.



When as many tiles as possible are pasted, find the sum of the areas not covered by the tiles.



output

Output the total area of ​​the part not covered by the tile. Also, output a line break at the end.

Example

Input

5 8
2 2


Output

8
"""

def calculate_uncovered_area(h: int, w: int, a: int, b: int) -> int:
    """
    Calculate the total area of the part not covered by the tiles on a rectangular wall.

    Parameters:
    h (int): The height of the wall.
    w (int): The width of the wall.
    a (int): The height of the tile.
    b (int): The width of the tile.

    Returns:
    int: The total area of the part not covered by the tiles.
    """
    high = h // a * a
    wide = w // b * b
    return h * w - high * wide