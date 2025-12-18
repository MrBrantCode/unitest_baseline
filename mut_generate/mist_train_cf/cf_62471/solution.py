"""
QUESTION:
Create a function `count_exam_pairs(n)` that calculates the number of subset pairs that need to be examined for equality in a set with `n` elements, where the set contains strictly ascending elements and already complies with the rule that if `B` encompasses more elements than `C`, then `S(B) > S(C)`. The function should not take any arguments other than `n`.
"""

import math

def count_exam_pairs(n):
    return math.factorial(n) / (math.factorial(2) * math.factorial(n - 2)) * (10/3)