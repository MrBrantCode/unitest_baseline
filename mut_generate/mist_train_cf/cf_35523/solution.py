"""
QUESTION:
Implement a function `find_pixel_differences(pixel_data_before, pixel_data_after)` that takes two 2D arrays of pixel data as input, where each pixel is represented by a tuple of RGB values, and returns a dictionary containing the indices of the pixels that have changed, along with their RGB values before the transformation. The dictionary should have the format `{index: {"before": [R, G, B]}}`.
"""

def find_pixel_differences(pixel_data_before, pixel_data_after):
    pixel_diff = {}
    height = len(pixel_data_before)
    width = len(pixel_data_before[0])

    for y in range(height):
        for x in range(width):
            if pixel_data_before[y][x] != pixel_data_after[y][x]:
                pixel_diff[f"({x}, {y})"] = {"before": list(pixel_data_before[y][x])}

    return pixel_diff