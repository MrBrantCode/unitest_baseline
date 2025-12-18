"""
QUESTION:
Implement a function named `get_output_length_after_conv` that calculates the output length of an image after applying a series of strided convolutions. The function should take four parameters: `width` and `height` of the input image, a list of `filter_sizes` representing the filter sizes used in the convolutions, and a constant `stride` value used in the convolutions. The function should return a tuple containing the resulting width and height after applying the convolutions. The input integers are positive, the length of `filter_sizes` is between 1 and 10, and all filter sizes are positive integers.
"""

from typing import List, Tuple

def get_output_length_after_conv(width: int, height: int, filter_sizes: List[int], stride: int) -> Tuple[int, int]:
    for filter_size in filter_sizes:
        width = (width - filter_size + stride) // stride
        height = (height - filter_size + stride) // stride
    return width, height