"""
QUESTION:
Implement a function `perform_color_mapping(image, cmap)` that takes a 3D image array and a 1D color map array as input. The function should update the blue and green color channels of the image using the color map values. For each pixel, the blue channel is updated with the value from the color map at index `(y * len(image[0]) + x) * 2`, and the green channel is updated with the value from the color map at index `(y * len(image[0]) + x) * 2 + 1`. Return the modified image.
"""

from typing import List

def perform_color_mapping(image: List[List[List[int]]], cmap: List[int]) -> List[List[List[int]]]:
    for y in range(len(image)):
        for x in range(len(image[0])):
            index = (y * len(image[0]) + x) * 2
            image[y][x][2] = cmap[index]
            image[y][x][1] = cmap[index+1]
    return image