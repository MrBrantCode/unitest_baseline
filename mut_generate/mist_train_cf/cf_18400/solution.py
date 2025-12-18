"""
QUESTION:
Write a recursive function `compute_average(lst)` to calculate the average of a list of numbers. The function should not use the built-in `sum()` function. If the list is empty, the function should return 0. If the list contains any NaN (Not a Number) values, the function should return NaN as the average.
"""

def compute_average(lst):
    if len(lst) == 0:
        return 0
    
    if lst[0] == float('nan'):
        return float('nan')
    
    def recursive_average(lst, total, count):
        if len(lst) == 0:
            return total / count if count > 0 else 0
        else:
            return recursive_average(lst[1:], total + lst[0], count + 1)
    
    return recursive_average(lst, 0, 0)