"""
QUESTION:
Write a function named `check_tuples` that takes two tuples `tuple1` and `tuple2` as input and returns `True` if each element in `tuple2` is smaller than its corresponding element in `tuple1`. The function should only consider elements up to the length of the shorter tuple, and it should return `False` if any pair of elements cannot be compared due to non-numeric values or if a corresponding element in `tuple1` is not greater than the element in `tuple2`.
"""

def check_tuples(tuple1, tuple2):
    try:
        for a, b in zip(tuple1, tuple2):
            if a <= b:
                return False
        return True
    except TypeError:
        return False