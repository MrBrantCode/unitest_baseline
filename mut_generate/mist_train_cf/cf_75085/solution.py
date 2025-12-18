"""
QUESTION:
Write a function `monotonic` that takes a list `l` and an optional boolean parameter `strict` (defaulting to `False`) as input. The function should return `True` if the input list or nested lists of elements are monotonically increasing or decreasing, factoring in the strictness requirement. If `strict` is `True`, adjacent elements must not be identical; otherwise, they may be the same. The function should work with both single lists and 2D lists, but may not handle lists of different depths.
"""

def monotonic(l, strict = False):
    def single_list_monotonic(sl):
        if strict:
            return all(x<y for x, y in zip(sl, sl[1:])) or all(x>y for x, y in zip(sl, sl[1:]))
        else:
            return all(x<=y for x, y in zip(sl, sl[1:])) or all(x>=y for x, y in zip(sl, sl[1:]))

    if all(isinstance(i, list) for i in l):
        return all(single_list_monotonic(sub_l) for sub_l in l)
    else:
        return single_list_monotonic(l)