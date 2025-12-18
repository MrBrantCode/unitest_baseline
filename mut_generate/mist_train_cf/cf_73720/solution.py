"""
QUESTION:
Write a function `garden_and_path_area(length, width, path_width)` that calculates the total area of a garden and a surrounding path. The garden has dimensions `length` and `width`, with `length > width`, and the path has a uniform width `path_width`. The path's area must be half the garden's area, and `path_width` must be one-tenth of the shortest side of the garden. The function should return the total area if the conditions are met; otherwise, return an error message.
"""

def garden_and_path_area(length, width, path_width):
    if not length > width:
        return "Error: Length of the garden must be greater than the width."
    if not path_width == width/10:
        return "Error: Width of the path should be one-tenth of the width of the garden."
    garden_area = length * width
    total_length = length + 2 * path_width
    total_width = width + 2 * path_width
    total_area = total_length * total_width
    path_area = total_area - garden_area
    if not path_area == garden_area / 2:
        return "Error: The area of the path must be half of the garden's area."
    return total_area