"""
QUESTION:
Write a function `calculate_output_shape` that takes an input shape `[batch_size, sequence_length, embedding_size, 1]` and a desired output shape `[batch_size, output_height, output_width, num_filters]`, and returns the values of `filter_shape`, `num_filters`, `n`, and `filter_size` that will achieve the desired output shape for the `pooled` tensor in a convolutional neural network with "VALID" padding and max-pooling operation using the same strides as the convolution operation.
"""

def calculate_output_shape(input_shape, desired_output_shape):
    batch_size, sequence_length, embedding_size, _ = input_shape
    output_height, output_width, num_filters = desired_output_shape[1:]

    # Calculate the value of n based on the input sequence length and desired output width
    n = sequence_length - (output_width - 1)

    # Calculate the filter size based on the input embedding size and desired output height
    filter_size = embedding_size - (output_height - 1)

    # Calculate the filter shape based on the filter size and input depth
    filter_shape = [filter_size, embedding_size, 1, num_filters]

    # Calculate the number of filters based on the desired output shape
    num_filters = num_filters

    return filter_shape, num_filters, n, filter_size