"""
QUESTION:
You are given two arithmetic progressions: a_1k + b_1 and a_2l + b_2. Find the number of integers x such that L ≤ x ≤ R and x = a_1k' + b_1 = a_2l' + b_2, for some integers k', l' ≥ 0.


-----Input-----

The only line contains six integers a_1, b_1, a_2, b_2, L, R (0 < a_1, a_2 ≤ 2·10^9,  - 2·10^9 ≤ b_1, b_2, L, R ≤ 2·10^9, L ≤ R).


-----Output-----

Print the desired number of integers x.


-----Examples-----
Input
2 0 3 3 5 21

Output
3

Input
2 4 3 0 6 17

Output
2
"""

from math import gcd

def exd_gcd(a, b):
    if a % b == 0:
        return (0, 1 if b > 0 else -1)
    (x, y) = exd_gcd(b, a % b)
    return (y, x - a // b * y)

def interval_intersect(a, b, c, d):
    if b <= a or d <= c:
        return 0
    if c < a:
        (a, b, c, d) = (c, d, a, b)
    if c < b:
        return min(b, d) - c
    else:
        return 0

def ceil(a, b):
    return (a + b - 1) // b

def count_common_integers(a1, b1, a2, b2, L, R):
    g = gcd(a1, a2)
    if (b1 - b2) % g != 0:
        return 0
    (k, l) = exd_gcd(a1, a2)
    l = -l
    k *= (b2 - b1) // g
    l *= (b2 - b1) // g
    d1 = a2 // g
    d2 = a1 // g
    assert k * a1 + b1 == l * a2 + b2
    (L1, R1) = (ceil(max(0, ceil(L - b1, a1)) - k, d1), ((R - b1) // a1 - k) // d1)
    (L2, R2) = (ceil(max(0, ceil(L - b2, a2)) - l, d2), ((R - b2) // a2 - l) // d2)
    return interval_intersect(L1, R1 + 1, L2, R2 + 1)