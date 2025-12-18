"""
QUESTION:
An array is called `zero-balanced` if its elements sum to `0` and for each positive element `n`, there exists another element that is the negative of `n`. Write a function named `ìsZeroBalanced` that returns `true` if its argument is `zero-balanced` array, else return `false`. Note that an `empty array` will not sum to `zero`.
"""

from collections import Counter

def isZeroBalanced(arr):
    if not arr:
        return False
    
    c = Counter(arr)
    return sum(arr) == 0 and all(c[k] == c[-k] for k in c)