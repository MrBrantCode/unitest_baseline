"""
QUESTION:
Define a function `f(n)` that calculates the count of dice displaying a 1 at the end of a process where a sequence of `n` dice are adjusted in a pattern based on their position. The adjustment pattern starts by increasing every second die by 1, then every third die, and so on, until every `n`th die. If a die reaches 6, it is reset to 1. Implement the function `f(n)` to compute the count of dice displaying 1 for a given `n`, with the restriction that `n` is a large integer (up to `10^36`).
"""

import math
def f(n):
    return n - int(math.sqrt(n))