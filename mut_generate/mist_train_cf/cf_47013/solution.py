"""
QUESTION:
Given a perimeter limit p, calculate S(p), the cumulative sum of the perimeters of all Heron envelopes with a perimeter that does not exceed p. A Heron envelope is a convex geometric figure composed of an isosceles triangle (the flap) positioned atop a rectangle where all sides and diagonals are integral, and the perpendicular height of the flap is less than the height of the rectangle. The function should only consider integral sides and diagonals.

Function Name: S(p)
Input: p, the perimeter limit
Restriction: p is an integer and p >= 0
"""

from math import isqrt, gcd

def S(p):
    """
    Calculate the cumulative sum of the perimeters of all Heron envelopes 
    with a perimeter that does not exceed p.

    Args:
    p (int): The perimeter limit.

    Returns:
    int: The cumulative sum of the perimeters of all Heron envelopes.

    """
    S = 0
    for n in range(1, isqrt(p//2)+1):
        for m in range(n+1, isqrt(p-2*n*n)+1, 2):
            if gcd(m, n) != 1: 
                continue

            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n  
            p_triplet = a+b+c

            if p_triplet > p:
                break

            if (c-b == 1 and 2*a >= b) or (c-a == 1 and 2*b >= a):
                S += p_triplet

    return S