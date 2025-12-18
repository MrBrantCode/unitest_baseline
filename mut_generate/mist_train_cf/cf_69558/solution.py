"""
QUESTION:
Write a function `minDifference(nums)` that determines the least disparity between the maximum and minimum values in the array `nums` after executing at most three operations, where each operation allows you to select a single element from `nums` and alter it to any numerical value. The function should take a list of integers `nums` as input and return the minimum possible disparity. The length of `nums` is between 1 and 10^5, and each element in `nums` is between -10^9 and 10^9.
"""

import bisect
import itertools
from collections import Counter

def minDifference(nums):
    A = sorted(Counter(nums).items())
    prefix = list(itertools.accumulate(x[1] for x in A))
    res = float('inf')
    for i, (x, y) in enumerate(A):
        if y > 3: return 0
        k = bisect.bisect_left(A, (x - 1, 0))
        if i - k < 3 - y:
            if not k: res = min(res, x)
        else:
            res = min(res,
                      x - A[k + 3 - y - (i - k == 3 - y)][0])
        k = bisect.bisect_right(A, (x + 1, 0))
        if k - 1 - i < 3 - y:
            if k == len(A): res = min(res, A[-1][0] - x)
        else:
            res = min(res,
                      A[k - 3 + y + (k - 1 - i == 3 - y)][0] - x)
    return res