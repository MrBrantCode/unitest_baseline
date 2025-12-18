"""
QUESTION:
You are given an integer `n` representing the size of an array and a list of `m` triplets, `queries`, where each triplet contains three integers `a`, `b`, and `k`. Implement the `arrayManipulation` function to return the maximum value in the resulting array after adding the value `k` to all elements in the inclusive range from index `a` to `b` for each query. 

Function signature: `arrayManipulation(n: int, queries: List[Tuple[int, int, int]]) -> int`
"""

from typing import List, Tuple

def arrayManipulation(n: int, queries: List[Tuple[int, int, int]]) -> int:
    arr = [0] * (n + 1)  
    for a, b, k in queries:
        arr[a - 1] += k  
        arr[b] -= k  
    max_val = 0
    prefix_sum = 0
    for val in arr:
        prefix_sum += val
        max_val = max(max_val, prefix_sum)
    return max_val