"""
QUESTION:
Calculate the total number of parameters in a convolutional neural network (CNN) layer. The function should take the input shape of the layer as a tuple (height, width, input_channels, output_channels) and return the total number of parameters, considering the weights and biases. The total number of parameters is calculated using the formula: Total parameters = (filter_width * filter_height * input_channels + 1) * output_channels.
"""

def entrance(input_shape):
    filter_height, filter_width, input_channels, output_channels = input_shape
    
    total_parameters = (filter_height * filter_width * input_channels + 1) * output_channels
    return total_parameters