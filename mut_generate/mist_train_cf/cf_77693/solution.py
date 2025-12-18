"""
QUESTION:
Write a function `count_indices` that takes two lists of integers `a1` and `a2` as input, where both lists have the same length. The function should return a tuple containing the count of indices where `a1` and `a2` have the same value and the sum of those indices.
"""

def count_indices(a1, a2):
    assert len(a1) == len(a2)

    matching_indices = [i for i in range(len(a1)) if a1[i] == a2[i]]
    return len(matching_indices), sum(matching_indices)