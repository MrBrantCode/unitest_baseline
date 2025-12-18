"""
QUESTION:
Create a function `unique_nth_root_and_mult` that takes an array of integers and three integer parameters `p`, `n`, and `q`. The function should compute the `p`th root of unique positive integers and the `n`th root of unique negative integers in the array, raise these roots to the power `q`, and then multiply the sum of these results by the count of unique positive integers and unique negative integers separately. If the array is empty, return `None`.
"""

import math

def unique_nth_root_and_mult(arr, p, n, q):
    if not arr:
        return None
    
    pos = [i for i in set(arr) if i > 0]
    neg = [i for i in set(arr) if i < 0]

    pos_res = sum(math.pow(i**(1/p), q) for i in pos) if pos else 0
    neg_res = sum(math.pow(-(-i) ** (1 / n), q) for i in neg) if neg else 0

    if pos and neg:
        mult = len(pos) * len(neg)
    elif pos:
        mult = len(pos)
    elif neg:
        mult = len(neg)
    else:
        mult = 1

    return mult * (pos_res - neg_res)