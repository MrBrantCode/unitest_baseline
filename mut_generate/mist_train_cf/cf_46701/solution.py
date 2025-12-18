"""
QUESTION:
Write a function `calculate_memory_footprint` that calculates the memory footprint for each layer in a neural network model. The model consists of three fully connected layers with the following specifications:

- The first layer has `input_shape[1]` neurons in the input layer and `num_units` neurons in the first layer.
- The second layer has `num_units` neurons in both the previous and current layers.
- The third layer has `num_units` neurons in the previous layer and `num_outputs` neurons in the current layer.

Assume the data type for parameters is `float32`, which requires 4 bytes per parameter. The function should return the memory footprint for each layer, considering both weights and biases.
"""

def calculate_memory_footprint(input_shape, num_units, num_outputs):
    """
    Calculate the memory footprint for each layer in a neural network model.

    Parameters:
    input_shape (tuple): The shape of the input data.
    num_units (int): The number of neurons in the first and second layers.
    num_outputs (int): The number of neurons in the output layer.

    Returns:
    tuple: A tuple containing the memory footprint for each layer in bytes.
    """

    # Calculate memory footprint for the first layer
    # Weights: input_shape[1] * num_units * 4 bytes
    # Bias: num_units * 4 bytes
    memory_footprint_first_layer = (input_shape[1] * num_units + num_units) * 4

    # Calculate memory footprint for the second layer
    # Weights: num_units * num_units * 4 bytes
    # Bias: num_units * 4 bytes
    memory_footprint_second_layer = (num_units * num_units + num_units) * 4

    # Calculate memory footprint for the third layer
    # Weights: num_units * num_outputs * 4 bytes
    # Bias: num_outputs * 4 bytes
    memory_footprint_third_layer = (num_units * num_outputs + num_outputs) * 4

    return memory_footprint_first_layer, memory_footprint_second_layer, memory_footprint_third_layer