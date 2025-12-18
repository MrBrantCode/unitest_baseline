"""
QUESTION:
Implement a function `calculate_integral_image` that takes a 2D list `grayscale_image` representing a grayscale image as input and returns the corresponding integral image. The integral image is a data structure where each pixel contains the sum of all the pixels above and to the left of it in the original image, inclusive. The function should initialize an integral image array of the same dimensions as the input grayscale image, with each element initially set to 0, and then calculate the integral image values based on the given grayscale image definition.
"""

from typing import List

def calculate_integral_image(grayscale_image: List[List[int]]) -> List[List[int]]:
    height, width = len(grayscale_image), len(grayscale_image[0])
    integral_image = [[0 for _ in range(width)] for _ in range(height)]

    integral_image[0][0] = grayscale_image[0][0]
    for j in range(1, width):
        integral_image[0][j] = integral_image[0][j-1] + grayscale_image[0][j]

    for i in range(1, height):
        integral_image[i][0] = integral_image[i-1][0] + grayscale_image[i][0]

    for i in range(1, height):
        for j in range(1, width):
            integral_image[i][j] = grayscale_image[i][j] + integral_image[i-1][j] + integral_image[i][j-1] - integral_image[i-1][j-1]

    return integral_image