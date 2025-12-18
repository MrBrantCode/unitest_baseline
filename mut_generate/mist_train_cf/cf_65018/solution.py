"""
QUESTION:
Write a function named `convolve` that performs a convolution operation on an image. The function should take three parameters: a 2D list representing the image, a 2D list representing the kernel, and a tuple representing the strides. Implement the convolution operation using the sliding window approach, where the kernel systematically scans the entire image from left to right, top to bottom, applying matrix multiplication of the corresponding pixels and summing all the multiplied values to result in one single output.
"""

def convolve(image, kernel, strides):
    """
    Perform a convolution operation on an image.

    Parameters:
    image (list): A 2D list representing the image.
    kernel (list): A 2D list representing the kernel.
    strides (tuple): A tuple representing the strides.

    Returns:
    list: The result of the convolution operation.
    """
    kernel_height, kernel_width = len(kernel), len(kernel[0])
    stride_height, stride_width = strides
    output_height = (len(image) - kernel_height) // stride_height + 1
    output_width = (len(image[0]) - kernel_width) // stride_width + 1
    output = [[0 for _ in range(output_width)] for _ in range(output_height)]

    for i in range(output_height):
        for j in range(output_width):
            for k in range(kernel_height):
                for l in range(kernel_width):
                    output[i][j] += image[i * stride_height + k][j * stride_width + l] * kernel[kernel_height - k - 1][kernel_width - l - 1]
    return output