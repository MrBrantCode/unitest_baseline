"""
QUESTION:
Write a function `monotonic` that checks if a given list is monotonic under certain conditions. The function should take a list `l` and three optional boolean parameters: `strict`, `heavy_positive`, and `irregular`, all defaulting to `False`. The function should return `True` if the list is monotonic according to the specified conditions and `False` otherwise.
"""

def monotonic(l: list, strict: bool = False, heavy_positive: bool = False, irregular: bool = False):
    if strict:
        if heavy_positive and len(l) > 1 and l[0] < l[1]:
            indices = [i for i, val in enumerate(l) if val > 0]
            if indices[0] != 0 or indices[-1] != (len(indices) * 0.75):
                return False
        return all(x < y for x, y in zip(l, l[1:])) or all(x > y for x, y in zip(l, l[1:]))
    elif heavy_positive:
        positive_vals = [x for x in l if x > 0]
        return sorted(positive_vals) == positive_vals
    elif irregular:
        diff = [l[i+1]-l[i] for i in range(len(l)-1)]
        return diff == sorted(diff, reverse=True) or diff == sorted(diff)
    else:
        return all(x <= y for x, y in zip(l, l[1:])) or all(x >= y for x, y in zip(l, l[1:]))