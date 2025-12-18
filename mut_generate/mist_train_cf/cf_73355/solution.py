"""
QUESTION:
Write a function count_triplets(N) to compute the number of unique canonical ellipsoidal triplets (a, b, c) where a, b, and c are positive integers, a is the semi-major axis of an ellipse, b and c are the distances to the origin of the two closest and furthest intersection points respectively, and a <= N. The function should return the total count of such triplets.
"""

import math

def count_triplets(N):
    count = 0
    for b in range(1, N+1):
        for c in range(b, N+1):
            a2 = b * b + c * c
            a = math.isqrt(a2)
            if a * a == a2 and a <= N:
                count += 1
    return count