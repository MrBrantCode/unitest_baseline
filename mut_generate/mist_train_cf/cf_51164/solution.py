"""
QUESTION:
Implement a function `median_mode` that takes a list of integers as input, calculates the median and mode without using built-in sorting functions or list sorting, and handles tuples containing negative entities. The function should return the median and mode as a tuple, where the mode is the most frequently occurring number in the list. If all numbers occur with the same frequency, the mode is considered `None`. If there are multiple modes, return one of them.
"""

def median_mode(numbers: list):
    count_dict = {}
    length = len(numbers)
    total_sum = 0
    
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
        total_sum += num
    
    median = total_sum / length
    mode = [k for k, v in count_dict.items() if v == max(count_dict.values())]
    if len(mode) == length:
        mode = None
    else:
        mode = mode[0]
        
    return median, mode