"""
QUESTION:
Implement a function `process_image` that processes an image by applying a specific operation. The function should take in a 2D list `image` representing the input image, a string `operation` specifying the operation to be applied, and an optional boolean parameter `copy` to determine whether the input image should be copied or modified in place.

The function should support two operations: "grayscale" and "invert". If `copy` is `True`, the function should create a new image and apply the operation to the new image, leaving the original image unchanged. If `copy` is `False`, the function should apply the operation directly to the input image.

The input image is a non-empty 2D list with dimensions m x n, where 1 <= m, n <= 1000, and each pixel value is an integer in the range 0 to 255. The function should return a 2D list representing the processed image.
"""

from typing import List

def process_image(image: List[List[int]], operation: str, copy: bool = False) -> List[List[int]]:
    if copy:
        processed_image = [row[:] for row in image]  
    else:
        processed_image = image  

    if operation == "grayscale":
        for i in range(len(processed_image)):
            for j in range(len(processed_image[0])):
                pixel = processed_image[i][j]
                processed_image[i][j] = (pixel + pixel + pixel) // 3  

    elif operation == "invert":
        for i in range(len(processed_image)):
            for j in range(len(processed_image[0])):
                processed_image[i][j] = 255 - processed_image[i][j]  

    return processed_image