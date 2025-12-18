"""
QUESTION:
Ever heard about Dijkstra's shallowest path algorithm? Me neither. But I can imagine what it would be.

You're hiking in the wilderness of Northern Canada and you must cross a large river. You have a map of one of the safer places to cross the river showing the depths of the water on a rectangular grid. When crossing the river you can only move from a cell to one of the (up to 8) neighboring cells. You can start anywhere along the left river bank, but you have to stay on the map.

An example of the depths provided on the map is 

```
[[2, 3, 2],
 [1, 1, 4],
 [9, 5, 2],
 [1, 4, 4],
 [1, 5, 4],
 [2, 1, 4],
 [5, 1, 2],
 [5, 5, 5],
 [8, 1, 9]]
```
If you study these numbers, you'll see that there is a path accross the river (from left to right) where the depth never exceeds 2. This path can be described by the list of pairs `[(1, 0), (1, 1), (2, 2)]`. There are also other paths of equal maximum depth, e.g., `[(1, 0), (1, 1), (0, 2)]`. The pairs denote the cells on the path where the first element in each pair is the row and the second element is the column of a cell on the path.

Your job is to write a function `shallowest_path(river)` that takes a list of lists of positive ints (or array of arrays, depending on language) showing the depths of the river as shown in the example above and returns a shallowest path (i.e., the maximum depth is minimal) as a list of coordinate pairs (represented as tuples, Pairs, or arrays, depending on language) as described above. If there are several paths that are equally shallow, the function shall return a shortest such path. All depths are given as positive integers.
"""

from heapq import *

MOVES = tuple(((dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if dx or dy))

def shallowest_path(river):
    (lX, lY) = (len(river), len(river[0]))
    pathDct = {}
    cost = [[(float('inf'), float('inf'))] * lY for _ in range(lX)]
    
    for x in range(lX):
        cost[x][0] = (river[x][0], 1)
    
    q = [(river[x][0], lY == 1, 1, (x, 0)) for x in range(lX)]
    heapify(q)
    
    while not q[0][1]:
        (c, _, steps, pos) = heappop(q)
        (x, y) = pos
        for (dx, dy) in MOVES:
            (a, b) = new = (x + dx, y + dy)
            if 0 <= a < lX and 0 <= b < lY:
                check = (nC, nS) = (max(c, river[a][b]), steps + 1)
                if cost[a][b] > check:
                    cost[a][b] = check
                    pathDct[new] = pos
                    heappush(q, (nC, b == lY - 1, nS, new))
    
    (path, pos) = ([], q[0][-1])
    while pos:
        path.append(pos)
        pos = pathDct.get(pos)
    
    return path[::-1]