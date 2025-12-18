"""
QUESTION:
Given is a string S, where each character is `0`, `1`, or `?`.

Consider making a string S' by replacing each occurrence of `?` with `0` or `1` (we can choose the character for each `?` independently). Let us define the unbalancedness of S' as follows:

* (The unbalancedness of S') = \max \\{ The absolute difference between the number of occurrences of `0` and `1` between the l-th and r-th character of S (inclusive) :\ 1 \leq l \leq r \leq |S|\\}



Find the minimum possible unbalancedness of S'.

Constraints

* 1 \leq |S| \leq 10^6
* Each character of S is `0`, `1`, or `?`.

Input

Input is given from Standard Input in the following format:


S


Output

Print the minimum possible unbalancedness of S'.

Examples

Input

0??


Output

1


Input

0??0


Output

2


Input

??00????0??0????0?0??00??1???11?1?1???1?11?111???1


Output

4
"""

from itertools import accumulate

def min_unbalancedness(S: str) -> int:
    N = len(S)
    A = [0] + list(accumulate((1 if s == '1' else -1 for s in S)))
    ma = max(A)
    cur = A[-1]
    C = [ma - cur]
    for a in reversed(A):
        cur = max(a, cur)
        C.append(ma - cur)
    (d, e) = (0, 0)
    (D, E) = (A[:], A[:])
    for (i, (s, c)) in enumerate(zip(S, reversed(C[:-1])), 1):
        if s == '?' and c >= d + 2:
            d += 2
        if s == '?' and c >= e + 1:
            e += 2
        D[i] += d
        E[i] += e
    return min(max(D) - min(D), max(E) - min(E))