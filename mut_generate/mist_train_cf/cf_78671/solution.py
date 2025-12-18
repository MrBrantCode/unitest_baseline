"""
QUESTION:
Write a function `median` that calculates the middle value of a list without using built-in sorting or median functions. The function should take two parameters: `l` (a list of numbers) and `cmp_func` (a callable comparison function). The function should remove any duplicate elements from the list, handle both even and odd length lists, and use the `cmp_func` to compare elements. If the list length is even, the function should return the average of the two middle elements if they are not the same, otherwise return the single middle element.
"""

def entrance(l: list, cmp_func: callable):
    l = list(set(l))  # remove duplicates
    n = len(l)
    mid = float('inf')
    mid_val = None

    for e in l:
        smaller = sum(1 for i in l if cmp_func(i, e) < 0)
        larger = sum(1 for i in l if cmp_func(i, e) > 0)
        if abs(smaller - larger) < mid:
            mid = abs(smaller - larger)
            mid_val = e

    # If the list length is even and there is another element with the same
    # amount of smaller and larger elements, take the average of these elements
    if n % 2 == 0:
        for e in l:
            if e != mid_val and abs(sum(1 for i in l if cmp_func(i, e) < 0) - sum(1 for i in l if cmp_func(i, e) > 0)) == mid:
                return (mid_val + e) / 2

    return mid_val