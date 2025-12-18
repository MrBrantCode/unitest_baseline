"""
QUESTION:
Create a function `remove_tuples(initial_tuple, remove_tuple)` that takes two tuples as input: `initial_tuple` and `remove_tuple`. The function should return a new tuple containing all elements from `initial_tuple` except those present in `remove_tuple`. The function should remove all occurrences of the tuples from `remove_tuple` from `initial_tuple`, not just the first occurrence. The function must handle duplicate tuples in `initial_tuple`.
"""

def remove_tuples(initial_tuple, remove_tuple):
    initials = list(initial_tuple)
    removes = list(remove_tuple)

    for r in removes:
        while r in initials:
            initials.remove(r)

    return tuple(initials)