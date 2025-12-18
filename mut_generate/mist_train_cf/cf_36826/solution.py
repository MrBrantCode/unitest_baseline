"""
QUESTION:
Write a function `find_bounding_box(f1)` that takes a 2D list `f1` representing a binary image as input, where 1 represents a white pixel and 0 represents a black pixel. The function should return a tuple of tuples representing the coordinates of the bounding box surrounding the white pixels in the format ((min_row, min_col), (max_row, max_col)). The bounding box is defined by the coordinates of its top-left (min_row, min_col) and bottom-right (max_row, max_col) corners.
"""

def find_bounding_box(f1):
    rows = len(f1)
    cols = len(f1[0])
    min_row, min_col, max_row, max_col = float('inf'), float('inf'), 0, 0
    
    for i in range(rows):
        for j in range(cols):
            if f1[i][j] == 1:
                min_row = min(min_row, i)
                min_col = min(min_col, j)
                max_row = max(max_row, i)
                max_col = max(max_col, j)
    
    return ((min_row, min_col), (max_row, max_col))