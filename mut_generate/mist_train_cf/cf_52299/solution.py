"""
QUESTION:
Find the function Q(n) which represents the number of 90-degree quadrilaterals for which the radius r of the inscribed circle is less than or equal to n. The function Q(n) should be calculated based on Pythagorean triples (a, b, c) where a and b are the lengths of two sides of the rectangle and c is the hypotenuse, and a <= 2n and b <= n. Implement the function Q(n) that takes an integer n as input and returns the number of 90-degree quadrilaterals that satisfy the condition r <= n.
"""

def entrance(n):
    counts = [0]*(2*n+1)
    quadrilaterals = 0

    for r in range(1, n+1):
        quadrilaterals += counts[r]
        for b in range(r+1, 2*n+1, 2):
            a = ((b*b - r*r) / 2)**0.5
            if int(a) != a: continue
            a = int(a)
            counts[b] += min(r, a+1) - max(b-a+1, 1) + 1

    return quadrilaterals