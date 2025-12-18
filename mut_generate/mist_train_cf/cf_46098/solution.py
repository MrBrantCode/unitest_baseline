"""
QUESTION:
Write a function `check_image_alignment` that checks if `imageAlign` should be exported based on the value of `hasImage`. The function should take two parameters: `hasImage` (a boolean) and `imageAlign` (a string). The function should return `imageAlign` only if `hasImage` is `True`. 

Note: The problem is not actually asking for a function, but rather how to conditionally export a prop in Svelte. However, the provided answer is in Python, so I've framed the question to match.
"""

def check_image_alignment(hasImage, imageAlign):
    """
    Checks if imageAlign should be exported based on the value of hasImage.

    Args:
        hasImage (bool): Whether an image exists.
        imageAlign (str): The alignment of the image.

    Returns:
        str or None: The image alignment if an image exists, otherwise None.
    """
    if hasImage:
        return imageAlign
    else:
        return None