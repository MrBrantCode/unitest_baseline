"""
QUESTION:
Define a function S(n) that represents the cumulative sum of the radii of the circumscribed circles of all triangles with integer sides where the radius does not surpass n and the triangle's sides do not exceed 10^7. Compute S(10^7) given that the radius of the circumscribed circle is also an integer.
"""

def S(n):
    from collections import defaultdict
    from itertools import count
    from math import sqrt

    limit = n
    perfsquares = defaultdict(list)
    for i in range(2, 2 * limit):
        iq = i*i
        if iq > 4 * limit * limit:
            break
        perfsquares[iq].append(i)

    total = 0
    for a in count(start=1):
        if a >= limit:
            break
        for b in range(a, limit):
            q = (a+b)**2 - a*b
            if q in perfsquares:
                for ab in perfsquares[q]:
                    c = ab // 2
                    if c < b or c >= limit:
                        continue
                    if a+b > c and b+c > a and c+a > b:
                        r = (a*b*c) // (ab - 2*c)
                        if r <= limit:
                            total += r
    return total