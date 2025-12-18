"""
QUESTION:
Create a function `intricate_monotonic` that takes a list `l` and five optional boolean parameters: `strict`, `zero_crossing`, `reverse`, `double_zero`, and `edge_cases`, all defaulting to `False`. The function should return `True` if the list is monotonic according to the specified conditions and `False` otherwise. 

The function should check for the following conditions:
- `strict`: If `True`, the list should be strictly monotonic.
- `reverse`: If `True`, the list should be monotonically decreasing instead of increasing.
- `zero_crossing`: If `True`, the function should check for zero-crossings (i.e., when the elements cross from negative to positive).
- `double_zero`: If `True`, the function should check for double zero-crossings and return `True` if the list crosses zero twice.
- `edge_cases`: If `True`, the function should ignore the first and last elements of the list when checking for monotonicity.
"""

def intricate_monotonic(l: list, strict: bool = False, zero_crossing: bool = False, reverse: bool = False, double_zero: bool = False, edge_cases: bool = False):
    if not l:
        return True

    if edge_cases:
        l = l[1:-1]
 
    if zero_crossing:
        zero_crossed = False
        for i in range(1, len(l)):
            if l[i-1] == 0 and l[i] > 0:
                if zero_crossed:
                    if double_zero:
                        return True
                    else:
                        return False
                else:
                    zero_crossed = True
    
    comparer = all if strict else any
    if reverse:
        return comparer(x>y for x, y in zip(l, l[1:]))
    else:
        return comparer(x<y for x, y in zip(l, l[1:]))