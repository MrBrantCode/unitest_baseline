"""
QUESTION:
Write a function `max_consecutive_sum` that takes a list of integers as input, where each integer is separated by a space, and returns the maximum sum of consecutive integers after replacing spaces with hyphens in each input integer. The function should take a list `arr` of length between 1 and 10^5, where each integer `x` is between -10^9 and 10^9.
"""

from typing import List

def max_consecutive_sum(arr: List[int]) -> int:
    max_sum = arr[0]
    current_sum = arr[0]
    for num in arr[1:]:
        num = int(str(num).replace(' ', '-'))
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum