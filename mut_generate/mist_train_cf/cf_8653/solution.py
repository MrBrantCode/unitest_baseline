"""
QUESTION:
Write a function named `check_overlap(rect1: Tuple[int, int, int, int], rect2: Tuple[int, int, int, int]) -> bool:` that takes two rectangles represented by their top-left and bottom-right coordinates as input and returns a boolean value indicating whether the two rectangles overlap or not. Each rectangle is represented by a tuple containing four integers in the format (x1, y1, x2, y2), where (x1, y1) is the top-left point and (x2, y2) is the bottom-right point. Two rectangles are considered to overlap if they have at least one common point on their boundary or inside the rectangle.
"""

from typing import Tuple

def is_rectangle_overlap(rect1: Tuple[int, int, int, int], rect2: Tuple[int, int, int, int]) -> bool:
    """
    Checks if two rectangles overlap.
    
    Args:
    rect1: A tuple containing the coordinates of the top-left and bottom-right points of the first rectangle.
    rect2: A tuple containing the coordinates of the top-left and bottom-right points of the second rectangle.
    
    Returns:
    True if the rectangles overlap, False otherwise.
    """
    
    # Unpack the coordinates of the rectangles
    x1, y1, x2, y2 = rect1
    a1, b1, a2, b2 = rect2
    
    # Check if one rectangle is on the left side of the other
    if x2 < a1 or a2 < x1:
        return False
    
    # Check if one rectangle is above the other
    if y1 < b2 or b1 < y2:
        return False
    
    # If none of the above conditions are met, the rectangles must overlap
    return True