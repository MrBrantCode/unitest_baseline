"""
QUESTION:
Implement a function `process_image` that takes in a 2D list representing an image and an integer representing the number of bytes per line in the image. The function should convert the image to grayscale by averaging the red, green, and blue color components for each pixel, replacing the original tuple with a single integer value representing the grayscale intensity. The function should return the modified grayscale image as a 2D list. The number of bytes per line is not required to be used in the calculation but must be included as a parameter.
"""

from typing import List, Tuple

def process_image(image: List[List[Tuple[int, int, int]]], bytes_per_line: int) -> List[List[int]]:
    grayscale_image = []
    for row in image:
        grayscale_row = []
        for pixel in row:
            grayscale_intensity = sum(pixel) // 3  # Calculate average of r, g, b values
            grayscale_row.append(grayscale_intensity)
        grayscale_image.append(grayscale_row)
    return grayscale_image