"""
QUESTION:
Given a target number `n`, find the smallest integer that can serve as the length of a cathetus in exactly `n` distinct integer sided right-angled triangles. The function should be named `smallest_cathetus(n)` and return the smallest cathetus length. The function should only consider Pythagorean triples where the catheti (shorter sides) are distinct and the lengths of the catheti are positive integers.
"""

def count_triples(y_limit):
    triangles = [0 for _ in range(y_limit)]
    for z in range(1, y_limit):
        for n in range(1, int((z**.5)+1)):
            if z % n == 0:
                m = z // n
                if (m - n) % 2:
                    a = m*m - n*n
                    b = 2*m*n
                    if a > b:
                        a, b = b, a
                    if a < y_limit:
                        triangles[a] += 1
                    if b < y_limit:
                        triangles[b] += 1
    return triangles

def smallest_cathetus(n):
    y_limit = n * 2
    while True:
        triangles = count_triples(y_limit)
        for x, count in enumerate(triangles):
            if count == n:
                return x
        y_limit += n