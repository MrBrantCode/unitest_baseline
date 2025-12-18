"""
QUESTION:
Write a function `calculate_total_parameters` that takes the input size, number of filters in each convolutional layer, kernel size, number of neurons in the fully connected layer, and the number of classes in the softmax layer as input and returns the total number of parameters in a convolutional neural network. The network has two convolutional layers with 3x3 kernels, followed by a fully connected layer, and a softmax layer. The input is an RGB image, and there are no pooling layers or dropout layers. The function should calculate the total number of parameters in the network.
"""

def calculate_total_parameters(input_size, num_filters_conv1, num_filters_conv2, num_neurons_fc, num_classes):
    """
    Calculate the total number of parameters in a convolutional neural network.

    Args:
    input_size (int): The size of the input image.
    num_filters_conv1 (int): The number of filters in the first convolutional layer.
    num_filters_conv2 (int): The number of filters in the second convolutional layer.
    num_neurons_fc (int): The number of neurons in the fully connected layer.
    num_classes (int): The number of classes in the softmax layer.

    Returns:
    int: The total number of parameters in the network.
    """

    # Calculate the number of parameters in the first convolutional layer
    params_conv1 = num_filters_conv1 * (3 * 3 * 3 + 1)

    # Calculate the number of parameters in the second convolutional layer
    params_conv2 = num_filters_conv2 * (3 * 3 * num_filters_conv1 + 1)

    # Calculate the number of parameters in the fully connected layer
    params_fc = num_neurons_fc * (input_size * input_size * num_filters_conv2 + 1)

    # Calculate the number of parameters in the softmax layer
    params_softmax = (num_neurons_fc + 1) * num_classes

    # Calculate the total number of parameters
    total_params = params_conv1 + params_conv2 + params_fc + params_softmax

    return total_params