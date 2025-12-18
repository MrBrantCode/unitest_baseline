"""
QUESTION:
Write a function `final_state(N, diffs)` that takes in an integer `N` and a list of differences `diffs` containing tuples of integers `(o, s)`. The function should initialize a list `out` of size `N+1` with the first element as 1 and the rest as 0, then apply the following operations: for each position `p` in `out`, update the value at position `p` and its subsequent positions based on the values of `o` and `s` in each tuple of `diffs`. The function should return the final state of the list `out` after applying all the operations.

The function should handle cases where the updated position exceeds `N`. The input `N` is a non-negative integer, and the list `diffs` contains zero or more tuples of integers `(o, s)`.
"""

from typing import List, Tuple

def final_state(N: int, diffs: List[Tuple[int, int]]) -> List[int]:
    out = [1] + [0]*N  
    for p in range(0, N+1):  
        x = out[p]  
        for (o, s) in diffs:  
            p += o  
            if p > N:  
                break
            out[p] += s  
    return out