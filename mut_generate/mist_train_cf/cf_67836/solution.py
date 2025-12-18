"""
QUESTION:
Write a function `median_and_mode` that takes a list of integers `l` as input and returns a tuple containing the median and mode of the list. The function should not use built-in functions to calculate the median and mode, except for sorting. It should work with lists of varying length (even or odd) and handle negative values and multiple identical entries. If there are multiple modes, the function should return `None` for the mode.
"""

def median_and_mode(l: list):
    l_sorted = sorted(l)
    l_len = len(l_sorted)
    median = None
    mode = None
    
    # calculate median
    if (l_len % 2 == 0): # even
        median =  (l_sorted[l_len // 2] + l_sorted[l_len // 2 - 1]) / 2
    else: # odd
        median = l_sorted[l_len // 2]
    
    # calculate mode
    freq_dict = {}
    for i in l_sorted:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1

    modes = [k for k, v in freq_dict.items() if v == max(freq_dict.values())]
    
    # return mode if single mode exists
    if len(modes) == 1:
        mode = modes[0]
    
    return median, mode