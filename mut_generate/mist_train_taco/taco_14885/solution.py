"""
QUESTION:
Description:

The mean (or average) is the most popular measure of central tendency; however it does not behave very well when the data is skewed (i.e. wages distribution). In such cases, it's better to use the median.

Your task for this kata is to find the median of an array consisting of n elements.

You can assume that all inputs are arrays of numbers in integer format. For the empty array your code should return `NaN` (false in JavaScript/`NULL` in PHP/`nil` in Ruby).

Examples:

Input `[1, 2, 3, 4]` --> Median `2.5`

Input `[3, 4, 1, 2, 5]` --> Median `3`
"""

import math

def calculate_median(arr):
    if not arr:
        return math.nan
    
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    
    if n % 2 == 1:
        return sorted_arr[n // 2]
    else:
        mid1 = sorted_arr[n // 2 - 1]
        mid2 = sorted_arr[n // 2]
        return (mid1 + mid2) / 2