"""
QUESTION:
Finish the following code:

def monotonic_extremes(l: list, strict: bool = False, extreme_count: int = 1):
    """
    Return True if list elements are monotonically increasing or decreasing, considering the strictness flag.
    If strict flag is True, adjacent elements must be different; otherwise, they can be the same. Moreover, the 
    monotonic property should hold true for at least `extreme_count` instances of adjacent elements.
"""

def monotonic_extremes(lst: list, strict: bool = False, extreme_count: int = 1):
    """
    Return True if list elements are monotonically increasing or decreasing, 
    considering the strictness flag. If strict flag is True, adjacent elements 
    must be different; otherwise, they can be the same. Moreover, the 
    monotonic property should hold true for at least `extreme_count` instances 
    of adjacent elements.
    """
    increasing = decreasing = True
    previous_diff = None
    
    for i in range(1, len(lst)):
        diff = lst[i] - lst[i - 1]
        
        if strict:
            if diff == 0:
                return False
            if previous_diff is not None and (diff * previous_diff < 0):
                extreme_count -= 1
        else:
            if diff < 0:
                increasing = False
            elif diff > 0:
                decreasing = False
            if previous_diff is not None and diff * previous_diff < 0:
                extreme_count -= 1
        
        previous_diff = diff
        
        if extreme_count <= 0:
            break
    
    return increasing or decreasing