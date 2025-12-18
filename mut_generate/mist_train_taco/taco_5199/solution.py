"""
QUESTION:
Two experienced climbers are planning a first-ever attempt: they start at two points of the equal altitudes on a mountain range, move back and forth on a single route keeping their altitudes equal, and finally meet with each other at a point on the route. A wise man told them that if a route has no point lower than the start points (of the equal altitudes) there is at least a way to achieve the attempt. This is the reason why the two climbers dare to start planning this fancy attempt.

The two climbers already obtained altimeters (devices that indicate altitude) and communication devices that are needed for keeping their altitudes equal. They also picked up a candidate route for the attempt: the route consists of consequent line segments without branches; the two starting points are at the two ends of the route; there is no point lower than the two starting points of the equal altitudes. An illustration of the route is given in Figure E.1 (this figure corresponds to the first dataset of the sample input).

<image>

Figure E.1: An illustration of a route

The attempt should be possible for the route as the wise man said. The two climbers, however, could not find a pair of move sequences to achieve the attempt, because they cannot keep their altitudes equal without a complex combination of both forward and backward moves. For example, for the route illustrated above: a climber starting at p1 (say A) moves to s, and the other climber (say B) moves from p6 to p5; then A moves back to t while B moves to p4; finally A arrives at p3 and at the same time B also arrives at p3. Things can be much more complicated and thus they asked you to write a program to find a pair of move sequences for them.

There may exist more than one possible pair of move sequences, and thus you are requested to find the pair of move sequences with the shortest length sum. Here, we measure the length along the route surface, i.e., an uphill path from (0, 0) to (3, 4) has the length of 5.



Input

The input is a sequence of datasets.

The first line of each dataset has an integer indicating the number of points N (2 ≤ N ≤ 100) on the route. Each of the following N lines has the coordinates (xi, yi) (i = 1, 2, ... , N) of the points: the two start points are (x1, y1) and (xN, yN); the line segments of the route connect (xi, yi) and (xi+1, yi+1) for i = 1, 2, ... , N - 1. Here, xi is the horizontal distance along the route from the start point x1, and yi is the altitude relative to the start point y1. All the coordinates are non-negative integers smaller than 1000, and inequality xi < xi+1 holds for i = 1, 2, .. , N - 1, and 0 = y1 = yN ≤ yi for i = 2, 3, ... , N - 1.

The end of the input is indicated by a line containing a zero.

Output

For each dataset, output the minimum sum of lengths (along the route) of move sequences until the two climbers meet with each other at a point on the route. Each output value may not have an error greater than 0.01.

Example

Input

6
0 0
3 4
9 12
17 6
21 9
33 0
5
0 0
10 0
20 0
30 0
40 0
10
0 0
1 2
3 0
6 3
9 0
11 2
13 0
15 2
16 2
18 0
7
0 0
150 997
300 1
450 999
600 2
750 998
900 0
0


Output

52.5
40.0
30.3356209304689
10078.072814085803
"""

from heapq import heappush, heappop

def find_minimum_meeting_distance(points):
    N = len(points)
    if N == 0:
        return 0.0

    YS = set((y for (x, y) in points))
    Q = points[:]
    for i in range(N - 1):
        (x0, y0) = points[i]
        (x1, y1) = points[i + 1]
        if y0 != y1:
            for y in YS:
                if y0 < y < y1 or y1 < y < y0:
                    x = (x1 - x0) / (y1 - y0) * (y - y0) + x0
                    assert x0 < x < x1 or x1 < x < x0
                    Q.append((x, y))
    Q.sort()

    def f(px, py, qx, qy):
        if py == qy:
            return abs(px - qx)
        return ((px - qx) ** 2 + (py - qy) ** 2) ** 0.5

    L = len(Q)
    INF = 10 ** 18
    que = [(0, 0, L - 1)]
    dist = {(0, L - 1): 0}
    dd = ((1, -1), (1, 0), (0, -1), (-1, 0), (0, 1), (1, 1), (-1, -1), (-1, 1))

    while que:
        (cost, a, b) = heappop(que)
        if cost < dist[a, b]:
            continue
        if a == b:
            return cost
        (ax, ay) = Q[a]
        (bx, by) = Q[b]
        for (da, db) in dd:
            na = a + da
            nb = b + db
            if not 0 <= na <= nb < L:
                continue
            (cx, cy) = Q[na]
            (dx, dy) = Q[nb]
            if cy != dy:
                continue
            n_cost = cost + f(ax, ay, cx, cy) + f(bx, by, dx, dy)
            key = (na, nb)
            if n_cost < dist.get(key, INF):
                dist[key] = n_cost
                heappush(que, (n_cost, na, nb))

    return -1.0