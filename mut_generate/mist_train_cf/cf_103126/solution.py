"""
QUESTION:
Write a function `find_max_value_within_range(lst, rng)` that finds the maximum value in list `lst` within the range defined by `rng`, where `rng` is a list containing the minimum and maximum values of the range. The function should return `None` if the range is invalid (i.e., the maximum value is less than or equal to the minimum value) or if no value in `lst` falls within the range and is greater than the minimum value.
"""

def find_max_value_within_range(lst, rng):
    min_val = min(rng)
    max_val = max(rng)
    
    if max_val <= min_val:
        return None
    
    max_value = None
    for num in lst:
        if min_val < num <= max_val:
            if max_value is None or num > max_value:
                max_value = num
    
    return max_value