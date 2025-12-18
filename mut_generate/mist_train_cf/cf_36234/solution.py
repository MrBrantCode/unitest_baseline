"""
QUESTION:
Implement a function `calculate_contrast_pixels(img, threshold)` that takes a 2D array `img` representing an image, where each element is a tuple of RGB values, and a positive integer `threshold` as input, and returns the number of pixels that satisfy the following conditions: 
1. The absolute difference between the average intensity of the current pixel and the pixel to its left is greater than the given threshold.
2. The absolute difference between the average intensity of the current pixel and the pixel to its right is greater than half of the given threshold.
"""

def calculate_contrast_pixels(img, threshold) -> int:
    contrast_pixels = 0
    for i in range(len(img)):
        for j in range(len(img[0])):
            if j > 0 and j < len(img[0]) - 1:
                r1, g1, b1 = img[i][j-1]
                r2, g2, b2 = img[i][j]
                r3, g3, b3 = img[i][j+1]

                ave1 = (r1 + g1 + b1) / 3
                ave2 = (r2 + g2 + b2) / 3
                ave3 = (r3 + g3 + b3) / 3

                if abs(ave2 - ave1) > threshold and abs(ave2 - ave3) > (threshold / 2):
                    contrast_pixels += 1

    return contrast_pixels