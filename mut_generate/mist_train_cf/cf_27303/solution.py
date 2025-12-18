"""
QUESTION:
Implement a function `is_cutout_too_large` that takes in five parameters: `x_span`, `y_span`, `z_span`, `time_points`, and `bit_depth`, representing the dimensions of a cutout request and the bit depth of the data. The function should calculate the total size of the cutout request in bytes and return `True` if the total size exceeds 1GB (1,073,741,824 bytes) when uncompressed, and `False` otherwise. The total size can be calculated as the product of `x_span`, `y_span`, `z_span`, the number of `time_points`, and the `bit_depth` divided by 8.
"""

def is_cutout_too_large(x_span, y_span, z_span, time_points, bit_depth):
    total_bytes = x_span * y_span * z_span * len(time_points) * (bit_depth / 8)
    return total_bytes > 1073741824  # 1GB in bytes