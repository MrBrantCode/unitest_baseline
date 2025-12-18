"""
QUESTION:
Create a function called `geom_mean` that calculates the geometric mean of a given array of numbers. The function should handle large input arrays (up to 10^6 elements) and large numbers (up to 10^324). The function should not use any external libraries or built-in functions that directly calculate the geometric mean, but using a built-in `math` module is allowed for other mathematical operations. The function should return 0 if the input array is empty or contains a non-positive number.
"""

import math

def geom_mean(array):
    if len(array) == 0:
        return 0
    sum_log = 0
    count = len(array)

    for num in array:
        if num > 0:
            sum_log += math.log(num)
        else:
            return 0

    return math.exp(sum_log/count)