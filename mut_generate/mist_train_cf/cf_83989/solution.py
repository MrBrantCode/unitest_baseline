"""
QUESTION:
Create a function named `median_and_standard_deviation` that takes a list of numbers as input and returns a tuple containing the median and standard deviation of the list. The function should handle lists with both even and odd numbers of elements, and it should calculate the median and standard deviation without sorting the list.
"""

import math
import heapq

def median_and_standard_deviation(numbers):
    count = len(numbers)
    if count == 0:
        return 0, 0

    mean = sum(numbers) / count
    std_dev = math.sqrt(sum((x - mean) ** 2 for x in numbers) / count)

    if count % 2 == 1:
        # odd
        median = heapq.nsmallest(count // 2 + 1, numbers)[-1]
    else:
        # even
        lo = heapq.nsmallest(count // 2, numbers)[-1]
        hi = heapq.nsmallest(count // 2 + 1, numbers)[-1]
        median = (lo + hi) / 2

    return median, std_dev