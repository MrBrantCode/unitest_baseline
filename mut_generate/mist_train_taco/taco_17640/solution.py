"""
QUESTION:
The full exploration sister is a very talented woman. Your sister can easily count the number of routes in a grid pattern if it is in the thousands. You and your exploration sister are now in a room lined with hexagonal tiles. The older sister seems to be very excited about the hexagon she sees for the first time. The older sister, who is unfamiliar with expressing the arrangement of hexagons in coordinates, represented the room in the coordinate system shown in Fig. 1.

<image> Figure 1

You want to move from one point on this coordinate system to another. But every minute your sister tells you the direction you want to move. Your usual sister will instruct you to move so that you don't go through locations with the same coordinates. However, an older sister who is unfamiliar with this coordinate system corresponds to the remainder of | x × y × t | (x: x coordinate, y: y coordinate, t: elapsed time [minutes] from the first instruction) divided by 6. Simply indicate the direction (corresponding to the number shown in the figure) and it will guide you in a completely random direction.

<image> Figure 2

If you don't want to hurt your sister, you want to reach your destination while observing your sister's instructions as much as possible. You are allowed to do the following seven actions.

* Move 1 tile to direction 0
* Move 1 tile to direction 1
* Move 1 tile in direction 2
* Move 1 tile in direction 3
* Move 1 tile in direction 4
* Move 1 tile in direction 5
* Stay on the spot



You always do one of these actions immediately after your sister gives instructions. The room is furnished and cannot be moved into the tiles where the furniture is placed. Also, movements where the absolute value of the y coordinate exceeds ly or the absolute value of the x coordinate exceeds lx are not allowed. However, the older sister may instruct such a move. Ignoring instructions means moving in a different direction than your sister indicated, or staying there. Output the minimum number of times you should ignore the instructions to get to your destination. Output -1 if it is not possible to reach your destination.

Constraints

* All inputs are integers
* -lx ≤ sx, gx ≤ lx
* -ly ≤ sy, gy ≤ ly
* (sx, sy) ≠ (gx, gy)
* (xi, yi) ≠ (sx, sy) (1 ≤ i ≤ n)
* (xi, yi) ≠ (gx, gy) (1 ≤ i ≤ n)
* (xi, yi) ≠ (xj, yj) (i ≠ j)
* 0 ≤ n ≤ 1000
* -lx ≤ xi ≤ lx (1 ≤ i ≤ n)
* -ly ≤ yi ≤ ly (1 ≤ i ≤ n)
* 0 <lx, ly ≤ 100

Input

The input is given in the following format.

> sx sy gx gy
> n
> x1 y1
> ...
> xi yi
> ...
> xn yn
> lx ly
>

here,

* sx, sy are the coordinates of the starting point
* gx, gy are the coordinates of the destination
* n is the number of furniture placed in the room
* xi, yi are the coordinates of the tile with furniture
* lx, ly are the upper limits of the absolute values ​​of the movable X and Y coordinates.

Output

Output in one line containing one integer. If you can reach your destination, print the number of times you ignore the minimum instructions. Output -1 if it is not possible to reach your destination.

Examples

Input

0 0 0 2
0
2 2


Output

0


Input

0 0 0 2
6
0 1
1 0
1 -1
0 -1
-1 -1
-1 0
2 2


Output

-1


Input

0 0 0 2
1
0 1
2 2


Output

1
"""

import heapq
import collections

def min_ignored_instructions(sx, sy, gx, gy, n, furniture, lx, ly):
    inf = 10 ** 20
    dd0 = [(0, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (0, 0)]
    dd1 = [(0, 1), (1, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (0, 0)]
    dd = [dd0, dd1]
    
    fs = set(furniture)
    
    def search(s, g):
        d = collections.defaultdict(lambda: inf)
        s = tuple(list(s) + [0])
        d[s] = 0
        q = []
        heapq.heappush(q, (0, s))
        v = collections.defaultdict(bool)
        while q:
            (k, u) = heapq.heappop(q)
            if v[u]:
                continue
            if (u[0], u[1]) == g:
                return k
            v[u] = True
            ddi = 0 if u[0] % 2 == 0 else 1
            (di, dj) = dd[ddi][abs(u[0] * u[1] * u[2]) % 6]
            nu = (u[2] + 1) % 6
            uv = (u[0] + di, u[1] + dj, nu)
            if d[uv] > k and abs(uv[0]) <= lx and abs(uv[1]) <= ly and (uv[0], uv[1]) not in fs:
                d[uv] = k
                heapq.heappush(q, (k, uv))
            vd = k + 1
            for (di, dj) in dd[ddi]:
                uv = (u[0] + di, u[1] + dj, nu)
                if v[uv] or abs(uv[0]) > lx or abs(uv[1]) > ly or (uv[0], uv[1]) in fs:
                    continue
                if d[uv] > vd:
                    d[uv] = vd
                    heapq.heappush(q, (vd, uv))
        return None
    
    r = search((sx, sy), (gx, gy))
    return -1 if r is None else r