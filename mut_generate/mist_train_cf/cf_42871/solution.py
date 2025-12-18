"""
QUESTION:
Implement a function called `resize_image` that takes a 2D list `image` and two integers `width` and `height` as input. The function should return a resized version of the input image, represented as a 2D list, with the specified `width` and `height`. The resized image should be created by sampling the input image at regular intervals. 

The input image dimensions will not exceed 1000x1000, and the `width` and `height` will be positive integers.
"""

def resized_image(image, width, height):
    original_height = len(image)
    original_width = len(image[0])

    new_image = []
    for i in range(height):
        row = []
        for j in range(width):
            x = j * original_width // width
            y = i * original_height // height
            row.append(image[y][x])
        new_image.append(row)

    return new_image