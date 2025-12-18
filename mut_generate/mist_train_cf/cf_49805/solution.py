"""
QUESTION:
Write a function `median_2d_list` that calculates the median value of a 2D list of integers. The function should flatten the 2D list, sort the numbers, and return the median value. If the total number of elements is even, the median should be the average of the two middle numbers. If the total number of elements is odd, the median should be the middle number.
"""

from typing import List

def median_2d_list(array: List[List[int]]):
    """Find the median value of a 2D list"""
    cleaned_list = [item for sublist in array for item in sublist]
    sorted_list = sorted(cleaned_list)
    length = len(sorted_list)

    if length % 2 == 0:  # Even number of elements
        return (sorted_list[length // 2 - 1] + sorted_list[length // 2]) / 2
    else:  # Odd number of elements
        return sorted_list[length // 2]