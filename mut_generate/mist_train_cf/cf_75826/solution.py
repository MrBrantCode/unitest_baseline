"""
QUESTION:
Implement a function `advanced_operation` that takes a list `l`, two integers `n` and `m`, and applies specific operations. The function should multiply an element by 2 if its 1-based index is divisible by `n`, reorder all elements with 1-based indices divisible by `m` in reverse order, and implement memoization to avoid recalculating results. Note that the input list should be converted to a tuple before passing to the function due to Python's caching limitations.
"""

from functools import lru_cache

@lru_cache(maxsize=None)
def advanced_operation(l: tuple, n: int, m: int):
    # step 1: Multiply an element by 2 if its index is divisible by n
    l = [i * 2 if idx % n == 0 else i for idx, i in enumerate(l, start=1)]
    
    # step 2: Reorder all elements with indices divisible by m in reverse order
    reorder_indices = [idx for idx in range(len(l)) if (idx+1) % m == 0]
    for i in range(len(reorder_indices) // 2):
        l[reorder_indices[i]], l[reorder_indices[-(i + 1)]] = l[reorder_indices[-(i + 1)]], l[reorder_indices[i]]
        
    return l