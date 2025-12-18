"""
QUESTION:
Write a function `largest_smallest_integers` that takes a list of integers as input and returns a tuple `(a, b, c, d, e, f)`. The function should return the highest negative even integer `a`, the highest non-negative even integer `b`, the smallest negative even integer `c`, the smallest non-negative even integer `d`, the smallest negative odd integer `e`, and the highest non-negative odd integer `f`. If no applicable numbers are available, return `None` for that value.
"""

def largest_smallest_integers(lst):
    highest_neg_even = highest_non_neg_even = smallest_neg_even = smallest_non_neg_even = smallest_neg_odd = highest_non_neg_odd = None
    
    for num in lst:
        if num%2 == 0: 
            if num < 0: 
                if highest_neg_even is None or highest_neg_even < num: 
                    highest_neg_even = num
                if smallest_neg_even is None or smallest_neg_even > num: 
                    smallest_neg_even = num
            else: 
                if highest_non_neg_even is None or highest_non_neg_even < num: 
                    highest_non_neg_even = num
                if smallest_non_neg_even is None or smallest_non_neg_even > num: 
                    smallest_non_neg_even = num
        else: 
            if num < 0: 
                if smallest_neg_odd is None or smallest_neg_odd > num: 
                    smallest_neg_odd = num
            else: 
                if highest_non_neg_odd is None or highest_non_neg_odd < num: 
                    highest_non_neg_odd = num
                    
    return (highest_neg_even, highest_non_neg_even, smallest_neg_even, smallest_non_neg_even, smallest_neg_odd, highest_non_neg_odd)