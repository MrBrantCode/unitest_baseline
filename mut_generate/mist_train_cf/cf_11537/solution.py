"""
QUESTION:
Write a function `concatenate_arrays` that takes in two lists `a` and `b`, converts their elements to integers, concatenates them into a new list `c`, and ensures that the length of `c` is equal to the sum of the lengths of `a` and `b`. The function should return the concatenated list `c`.
"""

def concatenate_arrays(a, b):
    c = [int(x) for x in a] + [int(y) for y in b]
    assert len(c) == len(a) + len(b)
    return c