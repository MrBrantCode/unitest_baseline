"""
QUESTION:
Implement the `infer_backprop_data_shape` function to calculate the shape of the input data after backpropagation in a group convolution operation. The function should take the following parameters: `input_shape` (a tuple of integers representing the dimensions of the input data), `in_channels` (an integer representing the number of input channels), `out_channels` (an integer representing the number of output channels), `kernel_size` (a tuple of integers representing the dimensions of the convolution kernel), `stride` (a tuple of integers representing the stride for the convolution operation), and `padding` (a tuple of integers representing the padding applied to the input data). The function should return the inferred shape of the input data after backpropagation as a tuple of integers.
"""

from typing import Tuple

def infer_backprop_data_shape(input_shape: Tuple[int], in_channels: int, out_channels: int, kernel_size: Tuple[int], stride: Tuple[int], padding: Tuple[int]) -> Tuple[int]:
    h_out = (input_shape[0] - 1) * stride[0] - 2 * padding[0] + kernel_size[0]
    w_out = (input_shape[1] - 1) * stride[1] - 2 * padding[1] + kernel_size[1]
    return (h_out, w_out, in_channels)