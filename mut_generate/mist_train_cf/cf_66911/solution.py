"""
QUESTION:
Write a Python function `normalize_image_data` that takes in a 3D array of image data with pixel values ranging from 0 to 255 and returns the normalized image data in the range (0,1). The function should not take any additional parameters other than the image data. Ensure that the output array has the same shape as the input array and the pixel values are normalized.
"""

def normalize_image_data(image_data):
    """
    Normalize image data to the range (0,1).
    
    Args:
    image_data (3D array): A 3D array of image data with pixel values ranging from 0 to 255.
    
    Returns:
    A 3D array of normalized image data in the range (0,1) with the same shape as the input array.
    """
    return image_data / 255.0