"""
QUESTION:
Implement a function `average` that calculates the average of elements in a potentially nested list containing strings, lists, and tuples. The function should utilize a custom comparison function `cmp_func` to compare string elements. The function should not use built-in functions for calculating the average.
"""

def average(l: list, cmp_func: callable):
    total = 0
    count = 0
    
    def add_value(el):
        nonlocal total, count
        if isinstance(el, (list, tuple)):
            for subel in el:
                add_value(subel)
        elif isinstance(el, str):
            total += cmp_func(el, "")
            count += 1
            
    add_value(l)
  
    return total / count if count > 0 else None