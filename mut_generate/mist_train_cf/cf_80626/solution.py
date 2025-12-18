"""
QUESTION:
Implement a function named `calculate_receptive_field` that calculates the receptive field of a dilated convolutional layer and a fully connected layer. The function should take in the parameters `kernel_size`, `dilation_rate`, and `num_layers` for the dilated convolutional layer, and the parameters `input_size` and `num_layers` for the fully connected layer. Assume that the fully connected layer does not have a receptive field in the classical sense but for the purpose of comparison, consider the entire input as its receptive field.
"""

def calculate_receptive_field(kernel_size, dilation_rate, num_layers, input_size=None):
    """
    Calculate the receptive field of a dilated convolutional layer and a fully connected layer.

    Args:
    kernel_size (int): The size of the kernel.
    dilation_rate (int): The dilation rate of the kernel.
    num_layers (int): The number of layers.
    input_size (int): The size of the input. Defaults to None.

    Returns:
    int: The receptive field.
    """
    if input_size is not None:
        # Receptive field of a fully connected layer
        return input_size
    else:
        # Receptive field of a dilated convolutional layer
        return (kernel_size - 1) * (dilation_rate ** num_layers - 1) // (dilation_rate - 1) + 1