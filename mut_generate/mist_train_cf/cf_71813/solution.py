"""
QUESTION:
Write a function `median` that takes a list `l` and a comparison function `_cmp_func` as parameters. The function should return the element from the list `l` which has the same number of elements smaller and larger than itself in the list. If there are two such elements and the list length is even, it will return the average of these elements. The comparison function `_cmp_func` should take two arguments and return a value that determines the order of the two elements.
"""

def median(l: list, _cmp_func: callable):
    l = list(set(l))
    n = len(l)
    mid = float('inf')
    mid_val = None

    for e in l:
        smaller = sum([1 for i in l if _cmp_func(i, e) < 0])
        larger = sum([1 for i in l if _cmp_func(i, e) > 0])
        if abs(smaller - larger) < mid:
            mid = abs(smaller - larger)
            mid_val = e

        if n % 2 == 0:
            for _e in l:
                if _e != mid_val and abs(sum(1 for i in l if _cmp_func(i, _e) < 0) - sum(1 for i in l if _cmp_func(i, _e) > 0)) == mid:
                    return (mid_val + _e) / 2

    return mid_val