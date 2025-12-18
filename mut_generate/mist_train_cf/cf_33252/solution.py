"""
QUESTION:
Implement a function named `getMinorMajorRatio` that takes a 2D array `image` and an integer `threshold` as input. The function should return the ratio of the count of elements in the image with values less than the threshold (minor elements) to the count of elements with values greater than or equal to the threshold (major elements). The function should handle the case where the count of major elements is zero, returning infinity if there are minor elements and 0.0 if there are none.
"""

from typing import List

def getMinorMajorRatio(image: List[List[int]], threshold: int) -> float:
    minor_count = sum(1 for row in image for pixel in row if pixel < threshold)
    major_count = sum(1 for row in image for pixel in row if pixel >= threshold)
    
    if major_count == 0:
        return float('inf') if minor_count > 0 else 0.0
    else:
        return minor_count / major_count