"""
QUESTION:
Create a function called `calculate_volume` that takes in the base length, slant height, and height of a parallelogram. Calculate and return the volume of the parallelogram, given that the volume is the product of the base length, slant height, and height.
"""

def calculate_volume(base_length, slant_height, height):
    """
    Calculate the volume of a parallelogram.

    Args:
        base_length (float): The base length of the parallelogram.
        slant_height (float): The slant height of the parallelogram.
        height (float): The height of the parallelogram.

    Returns:
        float: The volume of the parallelogram.
    """
    return base_length * slant_height * height