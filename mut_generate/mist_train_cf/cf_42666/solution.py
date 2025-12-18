"""
QUESTION:
Implement a function `performTransformation(center, polar, h, N, r1, r2)` that takes six parameters: a 2D point `center`, a 2D point `polar`, a scalar value `h`, an integer `N`, and two scalar values `r1` and `r2`. The function should perform a series of geometric transformations based on the given parameters and return the resulting points. The transformations involve calculating intermediate points and performing transformations using these points. The function should return a list of tuples containing the transformed points.
"""

import math

def performTransformation(center, polar, h, N, r1, r2):
    tau = 2 * math.pi  

    cq1 = (center[0] - polar[0], center[1] - polar[1])
    cqh = (center[0] - polar[0] * h, center[1] - polar[1] * h)
    transformed_points = []

    for n in range(N):
        a = n * tau / N
        b = a - tau / N
        p = (cqh[0] + r1 * math.cos(a) + r2 * math.sin(a), cqh[1] + r1 * math.cos(a) + r2 * math.sin(a))
        q = (cqh[0] + r1 * math.cos(b) + r2 * math.sin(b), cqh[1] + r1 * math.cos(b) + r2 * math.sin(b))
        transformed_points.append((p, q, cq1))

        p = (cqh[0] + r1 * math.cos(a) + r2 * math.sin(a), cqh[1] + r1 * math.cos(a) + r2 * math.sin(a))
        q = (cqh[0] + r1 * math.cos(b) + r2 * math.sin(b), cqh[1] + r1 * math.cos(b) + r2 * math.sin(b))
        transformed_points.append((p, q, cq1))

    return transformed_points