"""
QUESTION:
Write a function `process_images` that takes a list of image sizes as input and returns the preferred method for processing images of varying sizes for use in a Variational AutoEncoder (VAE). Consider the trade-offs between resizing, zero-padding, and using a Fully Convolutional Network (FCN) as the encoder.
"""

def process_images(image_sizes):
    """
    This function determines the preferred method for processing images of varying sizes 
    for use in a Variational AutoEncoder (VAE) based on the trade-offs between resizing, 
    zero-padding, and using a Fully Convolutional Network (FCN) as the encoder.

    Args:
        image_sizes (list): A list of image sizes.

    Returns:
        str: The preferred method for processing images.
    """
    
    # Calculate the variability of the image sizes
    size_variability = max(image_sizes) / min(image_sizes)
    
    # If the size variability is high, using an FCN is recommended
    if size_variability > 5:
        return "Fully Convolutional Network (FCN)"
    
    # If the size variability is moderate, zero-padding is recommended
    elif 2 <= size_variability <= 5:
        return "Zero-padding"
    
    # If the size variability is low, resizing is recommended
    else:
        return "Resizing"