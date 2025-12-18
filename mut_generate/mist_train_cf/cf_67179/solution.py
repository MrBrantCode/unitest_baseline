"""
QUESTION:
Write a function B(N) that calculates the count of unique biclinic integral quadrilaterals ABCD with integer sides where 1 ≤ AB < BC < CD < AD, the diagonal BD has an integer length, and O is the midpoint of BD, and the line segment AO also has an integer length, and AO = CO ≤ BO = DO. The function should return the count of unique biclinic integral quadrilaterals that fulfill the condition AB^2+BC^2+CD^2+AD^2 ≤ N. The input N is a large integer, and the output should be the count of unique biclinic integral quadrilaterals.
"""

from collections import defaultdict
from math import ceil, sqrt

def B(N):
    counts = defaultdict(int)
    cnt = 0
    limit = N

    for s in range(6, int(2 * sqrt(limit)) + 1):
        for a in range(s // 2 - 1, max((ceil(s / 3) - 1, s // 4)), -2):
            b = s - a

            ans1 = a*a + b*b
            if ans1 > limit:
                continue

            a, b = min(a, b), max(a, b)

            for c in range(a - 1, max((a - a // 2, ceil((b * 2) / 3))), -2):
                d = a - c
                ans2 = c*c + d*d

                if ans1 + ans2 > limit:
                    continue

                c, d = min(c, d), max(c, d)
                if counts[(a, c, b, d)]:
                    continue

                counts[(a, c, b, d)] = counts[(c, a, d, b)] = 1
                cnt += 1

    return cnt