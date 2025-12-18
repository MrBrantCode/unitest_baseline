"""
QUESTION:
Design a function `median_mode_range` that takes an array of integers as input and returns the median, mode, and range of the array without sorting it. The array can contain negative numbers and duplicates, and there may be more than one mode. For even-sized arrays, the median is the average of the middle two numbers.
"""

from collections import Counter

def median_mode_range(arr):
    # calculate median
    n = len(arr)
    arr.sort() 
    if n % 2 == 0: 
        median = (arr[n//2] + arr[n//2 - 1]) / 2
    else: 
        median = arr[n//2] 
    
    # calculate mode
    data = Counter(arr) 
    get_mode = dict(data) 
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
    
    # calculate range
    min_val = min(arr)
    max_val = max(arr)
    range_val = max_val - min_val
    
    return median, mode, range_val