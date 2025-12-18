"""
QUESTION:
Nukes has an integer that can be represented as the bitwise OR of one or more integers between A and B (inclusive). How many possible candidates of the value of Nukes's integer there are?

Constraints

* 1 ≤ A ≤ B < 2^{60}
* A and B are integers.

Input

The input is given from Standard Input in the following format:


A
B


Output

Print the number of possible candidates of the value of Nukes's integer.

Examples

Input

7
9


Output

4


Input

65
98


Output

63


Input

271828182845904523
314159265358979323


Output

68833183630578410
"""

def count_possible_candidates(A: int, B: int) -> int:
    if A == B:
        return 1
    
    t = A ^ B
    N = len(bin(t)) - 2
    t = 1 << N
    a = A & (t - 1)
    b = B & (t - 1)
    blen = len(bin(b)) - 2
    sb = b & (2 ** (blen - 1) - 1)
    
    if sb == 0:
        sblen = 0
    else:
        sblen = len(bin(sb)) - 2
    
    s = (1 << sblen) - 1
    ymax = b | s
    T = 1 << (N - 1)
    ans = T - a
    
    if ymax < T + a:
        ans += ymax - T + 1 + T - a
    else:
        ans += T
    
    return ans