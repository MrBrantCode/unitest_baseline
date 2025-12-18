"""
QUESTION:
Write a function `find_max_disparity(arr1, arr2, arr3)` that accepts three numerical arrays as input and returns the largest disparity between the sum of pairs of numbers from different arrays, where each array contributes at most one number to the pair. Optimize for speed and minimize space complexity. The function should handle non-empty input arrays.
"""

def find_max_disparity(arr1, arr2, arr3):
    # Ensuring that the lists are sorted
    arr1.sort()
    arr2.sort()
    arr3.sort()

    # Getting the min and max values
    min_val = min(arr1[0], arr2[0], arr3[0])
    max_val = max(arr1[-1], arr2[-1], arr3[-1])

    return max_val - min_val