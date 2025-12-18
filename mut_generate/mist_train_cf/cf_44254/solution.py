"""
QUESTION:
Design a function `find_largest_disparity` that takes two numerical arrays as input and returns the largest disparity between any two values from the arrays. The function must compare each value in the first array to each value in the second array to find the largest disparity. The function should be optimized for time complexity, achieving better than O(n^2) performance.
"""

def find_largest_disparity(array1, array2):
    max1 = max(array1)
    min1 = min(array1)
    max2 = max(array2)
    min2 = min(array2)
    return max(abs(max1 - min2), abs(max2 - min1))