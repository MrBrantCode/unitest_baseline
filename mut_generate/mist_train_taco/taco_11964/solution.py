"""
QUESTION:
Taro came to a square to look for treasure. There are many treasures buried in this square, but Taro has the latest machines, so he knows everything about where the treasures are buried. Since the square is very wide Taro decided to look for the treasure to decide the area, but the treasure is what treasure does not know immediately whether or not there in the area for a lot. So Taro decided to count the number of treasures in that area.

Constraints

> 1 ≤ n ≤ 5000
> 1 ≤ m ≤ 5 × 105
> | xi |, | yi | ≤ 109 (1 ≤ i ≤ n)
> | xi1 |, | yi1 |, | xi2 |, | yi2 | ≤ 109 (1 ≤ i ≤ m)
> xi1 ≤ xi2, yi1 ≤ yi2 (1 ≤ i ≤ m)
>

* All inputs are given as integers

Input

> n m
> x1 y1
> x2 y2
> ...
> xn yn
> x11 y11 x12 y12
> x21 y21 x22 y22
> ...
> xm1 ym1 xm2 ym2
>

* n represents the number of treasures buried in the square
* m represents the number of regions to examine
* The 2nd to n + 1 lines represent the coordinates where each treasure is buried.
* The n + 2nd to n + m + 1 lines represent each area to be examined.
* The positive direction of the x-axis represents the east and the positive direction of the y-axis represents the north.
* Each region is a rectangle, xi1 and yi1 represent the coordinates of the southwestern apex of the rectangle, and xi2 and yi2 represent the coordinates of the northeastern apex of the rectangle.

Output

> C1
> C2
> ...
> Cm
>

* Output the number of treasures contained in each area to each line

Examples

Input

3 1
1 1
2 4
5 3
0 0 5 5


Output

3


Input

4 2
-1 1
0 3
4 0
2 1
-3 1 5 1
4 0 4 0


Output

2
1


Input

2 3
0 0
0 0
-1 -1 1 1
0 0 2 2
1 1 4 4


Output

2
2
0


Input

5 5
10 5
-3 -8
2 11
6 0
-1 3
-3 1 3 13
-1 -1 9 5
-3 -8 10 11
0 0 5 5
-10 -9 15 10


Output

2
2
5
0
4
"""

import bisect

class Ruiwa:
    def __init__(self, a):
        self.H = h = len(a)
        self.W = w = len(a[0])
        self.R = r = a
        for i in range(h):
            for j in range(1, w):
                r[i][j] += r[i][j - 1]
        for i in range(1, h):
            for j in range(w):
                r[i][j] += r[i - 1][j]

    def search(self, x1, y1, x2, y2):
        if x1 > x2 or y1 > y2:
            return 0
        r = self.R
        rr = r[y2][x2]
        if x1 > 0 and y1 > 0:
            return rr - r[y1 - 1][x2] - r[y2][x1 - 1] + r[y1 - 1][x1 - 1]
        if x1 > 0:
            rr -= r[y2][x1 - 1]
        if y1 > 0:
            rr -= r[y1 - 1][x2]
        return rr

def count_treasures_in_regions(n, m, treasures, regions):
    xd = set()
    yd = set()
    for (x, y) in treasures:
        xd.add(x)
        yd.add(y)
    xl = sorted(list(xd))
    yl = sorted(list(yd))
    xx = {}
    yy = {}
    for i in range(len(xl)):
        xx[xl[i]] = i
    for i in range(len(yl)):
        yy[yl[i]] = i
    a = [[0] * (len(yl) + 1) for _ in range(len(xl) + 1)]
    for (x, y) in treasures:
        a[xx[x]][yy[y]] += 1
    rui = Ruiwa(a)
    result = []
    for (x1, y1, x2, y2) in regions:
        xx1 = bisect.bisect_left(xl, x1)
        yy1 = bisect.bisect_left(yl, y1)
        xx2 = bisect.bisect(xl, x2) - 1
        yy2 = bisect.bisect(yl, y2) - 1
        result.append(rui.search(xx1, yy1, xx2, yy2))
    return result