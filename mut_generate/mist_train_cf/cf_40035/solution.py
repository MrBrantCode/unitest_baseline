"""
QUESTION:
Write a function `apply_kernel_operation(kernel, image)` where:
- `kernel` is a 2D list representing the kernel matrix with odd dimensions.
- `image` is a 2D list representing the input image.

The function should return the processed image after applying the kernel operation. Ensure that the function handles edge cases, such as handling the borders of the image when applying the kernel operation, and clamp the resulting pixel values to the range 0-255.
"""

def apply_kernel_operation(kernel, image):
    def apply_kernel_pixel(kernel, image, x, y):
        kernel_size = len(kernel)
        offset = kernel_size // 2
        result = 0
        for i in range(kernel_size):
            for j in range(kernel_size):
                image_x = x - offset + i
                image_y = y - offset + j
                if 0 <= image_x < len(image) and 0 <= image_y < len(image[0]):
                    result += kernel[i][j] * image[image_x][image_y]
        return result

    processed_image = []
    for i in range(len(image)):
        row = []
        for j in range(len(image[0])):
            pixel_value = apply_kernel_pixel(kernel, image, i, j)
            row.append(max(0, min(255, pixel_value)))  
        processed_image.append(row)

    return processed_image