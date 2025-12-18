"""
QUESTION:
Implement the `pixels_per_image` property in the `ImagePlotter` class to calculate and return the total number of pixels in an image. The image is represented by a 2D grid where the number of rows corresponds to the height and the number of columns corresponds to the width. The `pixels_per_image` property should multiply the number of rows and columns in the grid to determine the total number of pixels.
"""

def pixels_per_image(grid):
    """
    Calculate the total number of pixels in the image.
    
    Parameters:
    grid (list): A 2D grid representing the image.
    
    Returns:
    int: The total number of pixels in the image.
    """
    return len(grid) * len(grid[0])