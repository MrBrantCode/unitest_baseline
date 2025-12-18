"""
QUESTION:
You are given two arrays `src` and `dst` of the same length `n` with elements 0, 1, or -1, representing "copy", "add", and "remove" operations, respectively. Write a function `canTransform` that takes in `src` and `dst` and returns `True` if it is possible to transform `src` into `dst` using the given operations while satisfying the conditions `src[0] == dst[0]` and `src[-1] == dst[-1]`, and `False` otherwise.
"""

from typing import List

def canTransform(src: List[int], dst: List[int]) -> bool:
    if len(src) != len(dst):
        return False
    
    n = len(src)
    src_sum = 0
    dst_sum = 0
    
    for i in range(n):
        if src[i] == 0:
            src_sum += 1
        elif src[i] == 1:
            dst_sum += 1
        else:
            dst_sum -= 1
        
        if src_sum > dst_sum or dst_sum > src_sum:
            return False
    
    return src_sum == dst_sum and src[0] == dst[0] and src[-1] == dst[-1]