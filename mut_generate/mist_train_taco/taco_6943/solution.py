"""
QUESTION:
problem

Given a sequence $ a_i $ of length $ N $. Output all integers $ K (1 \ le K \ le N) $ that satisfy the following conditions.

Condition: Well sorted $ a_1, \ cdots, a_K $ matches $ a_ {N-K + 1}, \ cdots, a_N $.





Example

Input

8
5 2 4 9 4 9 2 5


Output

1 2 4 6 7 8
"""

from collections import Counter

def find_well_sorted_indices(a):
    n = len(a)
    ans = []
    t1, t2 = Counter(), Counter()
    
    for i in range(n):
        t1.update([a[i]])
        t2.update([a[n - 1 - i]])
        t3 = t1 & t2
        t1 -= t3
        t2 -= t3
        if t1 == t2:
            ans.append(i + 1)
    
    return ans