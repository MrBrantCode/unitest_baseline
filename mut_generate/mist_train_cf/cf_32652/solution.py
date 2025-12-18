"""
QUESTION:
Write a function `total_pixel_difference(images)` that takes a sequence of images as input, where each image is a 3D array representing height, width, and color channels. The function should calculate the total pixel difference across all consecutive pairs of images by summing the absolute differences of corresponding pixels. The images are subtracted from each other in sequence, and the result should be returned as the total pixel difference. The function should work for any number of images and any dimensions of the images, as long as all images have the same dimensions.
"""

def total_pixel_difference(images):
    total_diff = 0
    for i in range(1, len(images)):
        pixel_diff = images[i][:, :, :] - images[i-1][:, :, :]
        total_diff += abs(pixel_diff).sum()
    return total_diff