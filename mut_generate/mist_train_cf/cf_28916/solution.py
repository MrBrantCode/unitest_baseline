"""
QUESTION:
Implement a function `resize_image(original_image, target_size)` that takes an original image size as a tuple of two integers representing the width and height, and a target size as a tuple of two integers representing the width and height, and returns the resized image size as a tuple of two integers representing the width and height. The function should resize the original image to the target size while maintaining the aspect ratio. The original image size and target size are both provided as tuples of two integers.
"""

from typing import Tuple

def resize_image(original_image: Tuple[int, int], target_size: Tuple[int, int]) -> Tuple[int, int]:
    original_width, original_height = original_image
    target_width, target_height = target_size

    # Calculate aspect ratio
    aspect_ratio = original_width / original_height

    # Adjust width and height based on aspect ratio
    if original_width > original_height:
        new_width = target_width
        new_height = int(target_width / aspect_ratio)
    else:
        new_height = target_height
        new_width = int(target_height * aspect_ratio)

    return new_width, new_height