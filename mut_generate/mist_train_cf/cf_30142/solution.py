"""
QUESTION:
Implement the `convolve_1d_with_padding` function to perform a 1-dimensional convolution operation with padding. The function should take a 1-dimensional input array, a 1-dimensional kernel array, and a padding type as input, and return the result of the convolution operation. The padding type can be "valid" for no padding or "same" for zero-padding to maintain the same output size as the input. The function should perform element-wise multiplication and summation to obtain the convolution result.
"""

def convolve_1d_with_padding(input_array, kernel_array, padding_type):
    input_size = len(input_array)
    kernel_size = len(kernel_array)
    output_size = input_size if padding_type == "valid" else input_size

    if padding_type == "same":
        pad_left = (kernel_size - 1) // 2
        pad_right = kernel_size - 1 - pad_left
        input_array = [0] * pad_left + input_array + [0] * pad_right

    result = []
    for i in range(output_size):
        if i + kernel_size <= len(input_array):
            result.append(sum(a * b for a, b in zip(input_array[i:i+kernel_size], kernel_array)))
        else:
            break

    return result