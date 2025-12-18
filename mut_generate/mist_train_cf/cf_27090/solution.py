"""
QUESTION:
Implement the `resize_image` function, which takes a 2D array `image` representing an image where each pixel is a tuple of RGB values, and a `scaling_factor` tuple of two integers representing the scaling factor for width and height. The function should return the resized image, maintaining the aspect ratio of the original image. The resized image should be created by repeating the pixels of the original image according to the scaling factor.
"""

def resize_image(image, scaling_factor):
    original_height = len(image)
    original_width = len(image[0])
    new_width = original_width * scaling_factor[0]
    new_height = original_height * scaling_factor[1]

    resized_image = []
    for i in range(new_height):
        row = []
        for j in range(new_width):
            original_row = min(i // scaling_factor[1], original_height - 1)
            original_col = min(j // scaling_factor[0], original_width - 1)
            row.append(image[original_row][original_col])
        resized_image.append(row)

    return resized_image