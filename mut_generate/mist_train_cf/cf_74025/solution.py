"""
QUESTION:
Write a function named `find_dissimilar_elements` that takes two tuples `t1` and `t2` as input and returns a dictionary where the keys are the dissimilar elements and the values are tuples. Each tuple value should contain two elements: the count of the dissimilar element and a string indicating the originating tuple ("tuple1" or "tuple2"). If a dissimilar element is found in both tuples, the function should return the count from both tuples as a list in the format [count from tuple1, count from tuple2] and the string "both". The function should handle nested tuples, lists, and sets in the input tuples by flattening them before comparing the elements.
"""

from collections import Counter
from collections.abc import Iterable


def find_dissimilar_elements(t1, t2):
    def flatten(coll):
        for i in coll:
            if isinstance(i, Iterable) and not isinstance(i, (str, bytes)):
                for subc in flatten(i):
                    yield subc
            else:
                yield i

    flat_t1 = list(flatten(t1))
    flat_t2 = list(flatten(t2))

    t1_counter = Counter(flat_t1)
    t2_counter = Counter(flat_t2)

    result = {}
    for key, value in t1_counter.items():
        if key not in t2_counter:
            result[key] = (value, 'tuple1')
        else:
            result[key] = ([value, t2_counter[key]], 'both')

    for key, value in t2_counter.items():
        if key not in t1_counter:
            result[key] = (value, 'tuple2')

    return result