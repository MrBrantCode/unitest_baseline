"""
QUESTION:
Write a function `calculate_new_dimensions` that takes the length of a rectangular prism field as input. The width is 45% of the length and the height is 50% of the width. Calculate the new width, height, and volume after increasing the width and height by 30% proportionally.
"""

def calculate_new_dimensions(length):
    """
    Calculate the new width, height, and volume after increasing the width and height of a rectangular prism by 30%.

    Args:
    length (float): The length of the rectangular prism.

    Returns:
    dict: A dictionary containing the new width, height, and volume.
    """
    width = length * 0.45
    height = width * 0.5

    # increase the width and height by 30%
    new_width = width * 1.3
    new_height = height * 1.3

    # new volume
    new_volume = length * new_width * new_height

    return {
        "new_width": new_width,
        "new_height": new_height,
        "new_volume": new_volume
    }