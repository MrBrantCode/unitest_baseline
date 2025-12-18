"""
QUESTION:
Write a function `resize_image` that takes the original image's height, width, maximum allowed height, and maximum allowed width as input and returns the new height and width for the resized image, maintaining the original aspect ratio and fitting within the maximum constraints. The function should return the original height and width if the image already fits within the maximum constraints. The input and output values are integers.
"""

def resize_image(height: int, width: int, max_height: int, max_width: int) -> (int, int):
    # Calculate the aspect ratio of the original image
    aspect_ratio = width / height

    # Check if the original image already fits within the maximum constraints
    if height <= max_height and width <= max_width:
        return height, width

    # Calculate the new height and width based on the maximum constraints and aspect ratio
    if height > max_height:
        new_height = max_height
        new_width = int(max_height * aspect_ratio)
        if new_width > max_width:
            new_width = max_width
            new_height = int(max_width / aspect_ratio)
    else:  # width > max_width
        new_width = max_width
        new_height = int(max_width / aspect_ratio)

    return new_height, new_width