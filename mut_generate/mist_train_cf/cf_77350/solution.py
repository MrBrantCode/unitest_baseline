"""
QUESTION:
Create a function `largest_smallest_integers(lst)` that takes a list of integers `lst` and returns a tuple `(a, b, c, d)`. The tuple values are defined as follows:
- `a`: the largest negative even integer in `lst`
- `b`: the smallest non-negative even integer in `lst`
- `c`: the largest negative odd integer in `lst`
- `d`: the smallest non-negative odd integer in `lst`
If there are no matching integers for any of the values, return `None` for that value.
"""

def largest_smallest_integers(lst):
    
    if not lst:
        return (None, None, None, None)

    all_negative = list(filter(lambda x: x<0, lst))
    all_non_negative = list(filter(lambda x: x>=0, lst))
    
    negative_even = [i for i in all_negative if i%2==0]
    negative_odd = [i for i in all_negative if i%2!=0]
    non_negative_even = [i for i in all_non_negative if i%2==0]
    non_negative_odd = [i for i in all_non_negative if i%2!=0]
    
    a = max(negative_even) if negative_even else None
    b = min(non_negative_even) if non_negative_even else None
    c = max(negative_odd) if negative_odd else None
    d = min(non_negative_odd) if non_negative_odd else None

    return a, b, c, d