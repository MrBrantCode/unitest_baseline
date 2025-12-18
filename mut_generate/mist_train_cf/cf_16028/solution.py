"""
QUESTION:
Write a function `validate_image` that checks if an uploaded image meets the minimum resolution and size requirements. The function should take two parameters: `width` and `height` representing the image dimensions in pixels, and `size` representing the file size in bytes. The image should have a minimum resolution of 1000x1000 pixels and be less than 10 MB (10,485,760 bytes) in size. The function should return `True` if the image meets the requirements and `False` otherwise.
"""

def validate_image(width, height, size):
    """
    Validate if an uploaded image meets the minimum resolution and size requirements.

    Args:
    width (int): The width of the image in pixels.
    height (int): The height of the image in pixels.
    size (int): The file size of the image in bytes.

    Returns:
    bool: True if the image meets the requirements, False otherwise.
    """
    min_resolution = (1000, 1000)
    max_size = 10 * 1024 * 1024  # 10 MB

    # Check if the image meets the minimum resolution requirement
    if width < min_resolution[0] or height < min_resolution[1]:
        return False

    # Check if the image is within the maximum file size limit
    if size >= max_size:
        return False

    # If both checks pass, the image meets the requirements
    return True