"""
QUESTION:
Implement a function `min_max_normalization` that takes in five parameters: `v`, `min_old`, `max_old`, `min_new`, and `max_new`, and returns the normalized value of `v` using the Min-Max normalization formula. The function should apply the formula `((max_new - min_new) / (max_old - min_old)) * (v - max_old) + max_new` if `v` is closer to `max_old`, and `((max_new - min_new) / (max_old - min_old)) * (v - min_old) + min_new` otherwise.
"""

def min_max_normalization(v, min_old, max_old, min_new, max_new):
    """
    This function applies the Min-Max normalization formula to a given value v.
    
    Parameters:
    v (float): The value to be normalized.
    min_old (float): The minimum value of the original range.
    max_old (float): The maximum value of the original range.
    min_new (float): The minimum value of the new range.
    max_new (float): The maximum value of the new range.
    
    Returns:
    float: The normalized value of v.
    """
    
    # Calculate the difference between max_new and min_new, and max_old and min_old
    range_new = max_new - min_new
    range_old = max_old - min_old
    
    # Check if v is closer to max_old
    if abs(v - max_old) < abs(v - min_old):
        # Apply the formula if v is closer to max_old
        return (range_new / range_old) * (v - max_old) + max_new
    else:
        # Apply the formula if v is closer to min_old
        return (range_new / range_old) * (v - min_old) + min_new