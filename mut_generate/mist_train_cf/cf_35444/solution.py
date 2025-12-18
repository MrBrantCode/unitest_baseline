"""
QUESTION:
Implement a function `lineQuadrangleIntersection` that determines whether a line segment intersects with a quadrangle in a 2D plane. The function should take three inputs: the line segment's start position, the line segment's end position, and the quadrangle's points as a list of four tuples. The function should return `True` if the line segment intersects with the quadrangle, considering the line segment as part of the intersection, and `False` otherwise.
"""

def lineQuadrangleIntersection(pRayStartPos, pRayEndPos, pQuadranglePointList):
    def vdiff(a, b):
        return (a[0] - b[0], a[1] - b[1])

    def vcross(a, b):
        return a[0] * b[1] - a[1] * b[0]

    def intersect(p1, p2, p3, p4):
        v1 = vdiff(p4, p3)
        v2 = vdiff(p1, p3)
        v3 = vdiff(p2, p1)
        cross1 = vcross(v1, v2)
        cross2 = vcross(v1, v3)
        if cross1 * cross2 < 0:
            v4 = vdiff(p2, p1)
            v5 = vdiff(p3, p1)
            v6 = vdiff(p4, p3)
            v7 = vdiff(p2, p3)
            cross3 = vcross(v4, v5)
            cross4 = vcross(v6, v7)
            if cross3 * cross4 < 0:
                return True
        return False

    vLineSlope = vdiff(pRayEndPos, pRayStartPos)
    vTriPolys = pQuadranglePointList
    vBackface = False
    vHitCount = 0

    for i in range(4):
        if intersect(pRayStartPos, pRayEndPos, vTriPolys[i], vTriPolys[(i + 1) % 4]):
            vHitCount += 1

    return vHitCount % 2 == 1