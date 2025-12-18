"""
QUESTION:
Implement a function `get_out_size` that calculates the output size of a convolutional or pooling layer given the input size, padding, dilation, kernel size, and stride. The function should take five parameters: `in_size` (integer input size), `padding` (integer padding size), `dilation` (integer dilation factor), `kernel_size` (integer kernel size), and `stride` (integer stride size), and return the calculated output size as an integer.
"""

def get_out_size(in_size, padding, dilation, kernel_size, stride):
    effective_kernel_size = dilation * (kernel_size - 1) + 1
    padded_input_size = in_size + 2 * padding
    out_size = ((padded_input_size - effective_kernel_size) // stride) + 1
    return out_size