"""
QUESTION:
You are given a convolutional neural network (CNN) architecture that applies a MaxPooling layer followed by a convolutional layer to the input data. Write a function `calculate_output_shape` that takes the input shape of the data in the form of (height, width, channels) and returns the output shape after the given operations. The MaxPooling layer has a pool size of (2, 2) with default strides, and the convolutional layer uses 'same' padding, resulting in no change to the spatial dimensions. The number of channels in the output is 128.
"""

def calculate_output_shape(input_shape):
    # MaxPooling layer reduces the spatial dimensions by half
    pool_size = (2, 2)
    output_height = input_shape[0] // pool_size[0]
    output_width = input_shape[1] // pool_size[1]
    
    # Convolutional layer with 'same' padding does not change the spatial dimensions
    output_channels = 128
    
    return (output_height, output_width, output_channels)