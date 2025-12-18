"""
QUESTION:
Create a function `monotonic_deep(nl: List[List[int]], strict: bool = False)` that evaluates if the elements within a sublist and across sublists follow an increasing or decreasing sequence. The function should consider a strictness parameter, where if `strict` is set to `True`, consecutive elements should not hold the same value, and if `False`, repetition is allowed. The function should return `True` if the list is monotonic and `False` otherwise, and print the sublist index that doesn't follow the pattern if it exists.
"""

from typing import List

def monotonic_deep(nl: List[List[int]], strict: bool = False):
    for i, l in enumerate(nl):
        if len(set(l)) != len(l) and strict:
            print(f"Sublist at {i} is not strictly monotonic")
            return False
        if sorted(l) != l and sorted(l, reverse=True) != l:
            print(f"Sublist at {i} is not monotonic")
            return False
    if sorted(nl, key=lambda x: x[0]) != nl \
            and sorted(nl, key=lambda x: x[0], reverse=True) != nl:
        print("Overall list is not monotonic")
        return False
    return True