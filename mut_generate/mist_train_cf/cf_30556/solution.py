"""
QUESTION:
Write a function `intersect` that takes two lists of integers `A` and `B` as input and returns a list of integers representing their intersection, with each element appearing as many times as it shows in both arrays. The function should have the following signature: `def intersect(A: List[int], B: List[int]) -> List[int]`. The input lists can contain duplicate elements.
"""

from collections import Counter
from typing import List

def intersect(A: List[int], B: List[int]) -> List[int]:
    count_A = Counter(A)
    count_B = Counter(B)
    res = []
    for num, freq in count_A.items():
        if num in count_B:
            res.extend([num] * min(freq, count_B[num]))
    return res