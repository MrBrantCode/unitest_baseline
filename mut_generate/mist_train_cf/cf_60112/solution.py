"""
QUESTION:
Write a function `advanced_monotonic(l: list, strict: bool = False)` that returns True if the numeric elements in the list are either monotonically increasing or decreasing, and False otherwise. The function should ignore non-numeric elements and consider the strictness factor: if strict is True, the sequence must be strictly increasing or decreasing (i.e., no duplicate consecutive elements), while if strict is False, the sequence can be non-strictly increasing or decreasing (i.e., duplicate consecutive elements are allowed).
"""

def advanced_monotonic(l: list, strict: bool = False):
    rising, falling = True, True
    prev_i = None
    for i in l:
        if not isinstance(i, (int, float)):
            continue
        if prev_i is not None:
            if strict:
                if i > prev_i:
                    falling = False
                elif i < prev_i:
                    rising = False
                else:
                    rising, falling = False, False
            else:
                if i > prev_i:
                    falling = False
                elif i < prev_i:
                    rising = False
        prev_i = i
    return rising or falling