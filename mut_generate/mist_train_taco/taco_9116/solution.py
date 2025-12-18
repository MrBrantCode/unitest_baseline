"""
QUESTION:
As meticulous Gerald sets the table and caring Alexander sends the postcards, Sergey makes snowmen. Each showman should consist of three snowballs: a big one, a medium one and a small one. Sergey's twins help him: they've already made n snowballs with radii equal to r1, r2, ..., rn. To make a snowman, one needs any three snowballs whose radii are pairwise different. For example, the balls with radii 1, 2 and 3 can be used to make a snowman but 2, 2, 3 or 2, 2, 2 cannot. Help Sergey and his twins to determine what maximum number of snowmen they can make from those snowballs.

Input

The first line contains integer n (1 ≤ n ≤ 105) — the number of snowballs. The next line contains n integers — the balls' radii r1, r2, ..., rn (1 ≤ ri ≤ 109). The balls' radii can coincide.

Output

Print on the first line a single number k — the maximum number of the snowmen. Next k lines should contain the snowmen's descriptions. The description of each snowman should consist of three space-separated numbers — the big ball's radius, the medium ball's radius and the small ball's radius. It is allowed to print the snowmen in any order. If there are several solutions, print any of them.

Examples

Input

7
1 2 3 4 5 6 7


Output

2
3 2 1
6 5 4


Input

3
2 2 3


Output

0
"""

from heapq import heappop, heappush, heapify
from collections import defaultdict

def max_snowmen(n, radii):
    H = defaultdict(int)
    for r in radii:
        H[r] += 1
    
    D = [(-1 * v, k) for (k, v) in H.items()]
    heapify(D)
    
    ret = []
    while len(D) > 2:
        (a, b, c) = (heappop(D), heappop(D), heappop(D))
        ret.append(sorted([a[1], b[1], c[1]], reverse=True))
        for (x, xi) in ((i + 1, j) for (i, j) in (a, b, c)):
            if x:
                heappush(D, (x, xi))
    
    return len(ret), ret