"""
QUESTION:
Implement a function named `monotonic` that checks if the elements of a given list are monotonically increasing or decreasing. The function should consider the following conditions: 

- `strict`: if `True`, the function should return `True` only if neighboring elements are strictly increasing or decreasing (i.e., they cannot be identical).
- `heavy_positive`: if `True`, the function should consider a distribution skewed towards high numbers.
- `irregular`: if `True`, the function should check for monotonicity with non-uniform rate of change.

The function should return `True` if the list is monotonically increasing or decreasing based on the given conditions, and `False` otherwise.
"""

def monotonic(l: list, strict: bool = False, heavy_positive: bool = False, irregular: bool = False):
    if strict:
        if heavy_positive and len(l) > 1 and l[0] < l[1]:
            indices = [i for i, val in enumerate(l) if val > 0]
            if len(indices) == 0 or indices[-1] - indices[0] < len(indices) * 0.75:
                return False
        return all(x < y for x, y in zip(l, l[1:])) or all(x > y for x, y in zip(l, l[1:]))
    elif heavy_positive:
        positive_vals = [x for x in l if x > 0]
        return l == sorted(positive_vals)
    elif irregular:
        diff = [l[i+1]-l[i] for i in range(len(l)-1)]
        return diff == sorted(diff, reverse=True) or diff == sorted(diff)
    else:
        return all(x <= y for x, y in zip(l, l[1:])) or all(x >= y for x, y in zip(l, l[1:]))