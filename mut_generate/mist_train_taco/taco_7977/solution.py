"""
QUESTION:
Victor and Peter are playing hide-and-seek. Peter has hidden, and Victor is to find him. In the room where they are playing, there is only one non-transparent wall and one double-sided mirror. Victor and Peter are points with coordinates (xv, yv) and (xp, yp) respectively. The wall is a segment joining points with coordinates (xw, 1, yw, 1) and (xw, 2, yw, 2), the mirror — a segment joining points (xm, 1, ym, 1) and (xm, 2, ym, 2).

If an obstacle has a common point with a line of vision, it's considered, that the boys can't see each other with this line of vision. If the mirror has a common point with the line of vision, it's considered, that the boys can see each other in the mirror, i.e. reflection takes place. The reflection process is governed by laws of physics — the angle of incidence is equal to the angle of reflection. The incident ray is in the same half-plane as the reflected ray, relative to the mirror. I.e. to see each other Victor and Peter should be to the same side of the line, containing the mirror (see example 1). If the line of vision is parallel to the mirror, reflection doesn't take place, and the mirror isn't regarded as an obstacle (see example 4).

Victor got interested if he can see Peter, while standing at the same spot. Help him solve this problem.

Input

The first line contains two numbers xv and yv — coordinates of Victor.

The second line contains two numbers xp and yp — coordinates of Peter.

The third line contains 4 numbers xw, 1, yw, 1, xw, 2, yw, 2 — coordinates of the wall.

The forth line contains 4 numbers xm, 1, ym, 1, xm, 2, ym, 2 — coordinates of the mirror.

All the coordinates are integer numbers, and don't exceed 104 in absolute value. It's guaranteed, that the segments don't have common points, Victor and Peter are not on any of the segments, coordinates of Victor and Peter aren't the same, the segments don't degenerate into points.

Output

Output YES, if Victor can see Peter without leaving the initial spot. Otherwise output NO.

Examples

Input

-1 3
1 3
0 2 0 4
0 0 0 1


Output

NO


Input

0 0
1 1
0 1 1 0
-100 -100 -101 -101


Output

NO


Input

0 0
1 1
0 1 1 0
-1 1 1 3


Output

YES


Input

0 0
10 0
100 100 101 101
1 0 3 0


Output

YES
"""

def can_victor_see_peter(xv, yv, xp, yp, xw1, yw1, xw2, yw2, xm1, ym1, xm2, ym2):
    def a(x1, y1, x2, y2, x3, y3, x4, y4):
        if x1 == x2:
            if x3 == x4:
                return False
            else:
                k2 = (y3 - y4) / (x3 - x4)
                b2 = y3 - k2 * x3
                return min(y3, y4) <= k2 * x1 + b2 <= max(y3, y4) and min(y1, y2) <= k2 * x1 + b2 <= max(y1, y2) and (min(x3, x4) <= x1 <= max(x3, x4)) and (min(x1, x2) <= x1 <= max(x1, x2))
        elif x3 == x4:
            k1 = (y1 - y2) / (x1 - x2)
            b1 = y1 - k1 * x1
            return min(y3, y4) <= k1 * x3 + b1 <= max(y3, y4) and min(y1, y2) <= k1 * x3 + b1 <= max(y1, y2) and (min(x3, x4) <= x3 <= max(x3, x4)) and (min(x1, x2) <= x3 <= max(x1, x2))
        else:
            k1 = (y1 - y2) / (x1 - x2)
            b1 = y1 - k1 * x1
            k2 = (y3 - y4) / (x3 - x4)
            b2 = y3 - k2 * x3
            if k1 == k2:
                return b1 == b2 and min(x1, x2) <= min(x3, x4) <= max(x1, x2) and (min(y1, y2) <= min(y3, y4) <= max(y1, y2))
            x = (b2 - b1) / (k1 - k2)
            y = k1 * x + b1
            return min(y3, y4) <= y <= max(y3, y4) and min(y1, y2) <= y <= max(y1, y2) and (min(x3, x4) <= x <= max(x3, x4)) and (min(x1, x2) <= x <= max(x1, x2))

    def b(xm1, xm2, ym1, ym2, x, y):
        if ym1 == ym2:
            xi = x
            yi = 2 * ym1 - y
        elif xm1 == xm2:
            yi = y
            xi = 2 * xm1 - x
        else:
            k1 = -(xm1 - xm2) / (ym1 - ym2)
            b1 = y - k1 * x
            k2 = (ym1 - ym2) / (xm1 - xm2)
            b2 = ym1 - k2 * xm1
            x1 = (b2 - b1) / (k1 - k2)
            xi = 2 * x1 - x
            yi = k1 * xi + b1
        return [xi, yi]

    (xw3, yw3) = b(xm1, xm2, ym1, ym2, xw1, yw1)
    (xw4, yw4) = b(xm1, xm2, ym1, ym2, xw2, yw2)

    if a(xv, yv, xp, yp, xw1, yw1, xw2, yw2) or a(xv, yv, xp, yp, xm1, ym1, xm2, ym2):
        (xip, yip) = b(xm1, xm2, ym1, ym2, xp, yp)
        if [xip, yip] != [xv, yv] and a(xv, yv, xip, yip, xm1, ym1, xm2, ym2) and (not a(xv, yv, xip, yip, xw1, yw1, xw2, yw2)) and (not a(xv, yv, xip, yip, xw3, yw3, xw4, yw4)):
            return 'YES'
        else:
            return 'NO'
    else:
        return 'YES'