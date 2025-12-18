"""
QUESTION:
Write a function `find_median` that takes a list of floating-point numbers as input, filters out incorrect values, removes duplicates, and efficiently calculates the median. The function should handle a large dataset and return the median as a float. The input list may contain incorrect values such as strings, dictionaries, or None, and may not be ordered.
"""

import heapq

def find_median(nums):
    nums = [float(n) for n in nums if isinstance(n, (int, float))]
    if len(nums) == 0:
        return None

    nums = list(set(nums)) # Eliminating duplicates

    lower_half = [] 
    upper_half = [] 

    for num in nums:
        if not upper_half or num > upper_half[0]:
            heapq.heappush(upper_half,num)
        else:
            heapq.heappush(lower_half,-num)

        if len(lower_half) - len(upper_half) > 1:
            root = -heapq.heappop(lower_half)
            heapq.heappush(upper_half, root)
        elif len(upper_half) - len(lower_half) > 1:
            root = heapq.heappop(upper_half)
            heapq.heappush(lower_half, -root)

    if len(lower_half) == len(upper_half):
        return (-lower_half[0]+upper_half[0]) / 2.0
    elif len(lower_half) > len(upper_half):
        return -lower_half[0]
    else:
        return upper_half[0]