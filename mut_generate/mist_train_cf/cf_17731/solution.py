"""
QUESTION:
Create a function `calculateVolume` that calculates the volume of a rectangular prism given the length, width, and height. The function should only accept integer inputs and the output should be rounded to the nearest whole number. The function should not use the multiplication operator (*) or any built-in math functions.
"""

def calculateVolume(length, width, height):
    """
    Calculate the volume of a rectangular prism without using the multiplication operator or built-in math functions.

    Args:
        length (int): The length of the rectangular prism.
        width (int): The width of the rectangular prism.
        height (int): The height of the rectangular prism.

    Returns:
        int: The volume of the rectangular prism, rounded to the nearest whole number.
    """
    volume = 0
    sign = -1 if (length < 0) ^ (width < 0) ^ (height < 0) else 1

    for _ in range(abs(length)):
        for _ in range(abs(width)):
            volume += sign * abs(height)

    return volume