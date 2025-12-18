"""
QUESTION:
Create a function `is_geometric_progression(lst)` that takes a list of numeric strings as input and returns `True` if the list represents a geometric progression, `False` otherwise. The function should handle lists with less than three elements and lists containing non-numeric strings.
"""

def is_geometric_progression(lst):
    if len(lst) < 3:  
        return False
    try:
        lst = [int(i) for i in lst]
    except:
        return "Error: Input list should only contain numeric strings"

    common_ratio = lst[1] / float(lst[0])

    for i in range(1, len(lst)):
        if lst[i] / float(lst[i-1]) != common_ratio:
            return False
    return True