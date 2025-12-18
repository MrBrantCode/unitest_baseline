"""
QUESTION:
Write a function named `conv2d_feature_maps` that determines the possible number of feature maps in a Conv2D layer of a convolutional neural network. The Conv2D layer has a filter size of (3, 3), uses the 'relu' activation function, and 'same' padding. The function should consider the input image size of 128*128.
"""

def conv2d_feature_maps(input_size, filter_size=(3, 3)):
    """
    Determine the possible number of feature maps in a Conv2D layer.

    Args:
        input_size (int): The size of the input image.
        filter_size (tuple): The size of the filter (default is (3, 3)).

    Returns:
        list: A list of possible number of feature maps.
    """
    return [2**i for i in range(5, 11)]  # 32 to 1024