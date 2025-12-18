"""
QUESTION:
Implement the `convolve` function, which takes the original pixel matrix `pixel`, a kernel matrix `kernel`, and the coordinates `x` and `y` of the current pixel, and returns the result of applying the kernel to the pixel. Assume `pixel` and `kernel` are properly formatted and have valid dimensions. The function should handle edge cases where the kernel extends beyond the pixel matrix boundaries.
"""

def convolve(pixel, kernel, x, y):
    height, width = len(pixel), len(pixel[0])
    kernel_height, kernel_width = len(kernel), len(kernel[0])
    result = [0, 0, 0]  # Initialize the result for RGB channels

    for i in range(kernel_height):
        for j in range(kernel_width):
            pixel_x = x - kernel_height // 2 + i
            pixel_y = y - kernel_width // 2 + j

            if 0 <= pixel_x < height and 0 <= pixel_y < width:
                for c in range(3):  # Iterate over RGB channels
                    result[c] += pixel[pixel_x][pixel_y][c] * kernel[i][j]

    return [int(val) for val in result]  # Convert the result to integer pixel values