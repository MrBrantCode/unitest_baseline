"""
QUESTION:
Implement a function `maze3` that takes as input a 2D grid `maze` representing a maze with walls (`1`), empty spaces (`0`), and portals (`2`), the `start` position, the `destination` position, and the positions of two portals (`portal1` and `portal2`). The function should return the shortest distance for a ball to stop at the `destination` from the `start` position by rolling up, down, left, or right. If the ball cannot stop at `destination`, return `-1`. The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included), where traveling through a portal counts as 1 move.

Constraints: 
- `m == maze.length`
- `n == maze[i].length`
- `1 <= m, n <= 100`
- `maze[i][j]` is `0`, `1`, or `2`.
- `start.length == 2`
- `destination.length == 2`
- `portal1.length == 2`
- `portal2.length == 2`
- `0 <= startrow, destinationrow, portal1row, portal2row <= m`
- `0 <= startcol, destinationcol, portal1col, portal2col <= n`
"""

from collections import deque
from heapq import heappop, heappush

def maze3(maze, start, destination, portal1, portal2):
    # Add portal mapping
    maze[portal1[0]][portal1[1]] = maze[portal2[0]][portal2[1]] = '2'
    portals = [portal1, portal2] if portal1 < portal2 else [portal2, portal1]
    portal_dict = {tuple(portals[0]): tuple(portals[1]), tuple(portals[1]): tuple(portals[0])}

    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Edit destination to include rolling direction and distance. Initialize distance to inf.
    dest_node = tuple(destination + [0, 0])
    distances = {(i, j, dx, dy): float('inf') for i in range(rows) for j in range(cols) for dx, dy in directions}
    distances[tuple(start + [0, 0])] = 0

    heap = [(0, tuple(start + [0, 0]))]
    while heap:
        current_dist, (x, y, dx, dy) = heappop(heap)

        if (x, y, dx, dy) == dest_node:
            return current_dist

        for ndx, ndy in directions:
            nx, ny, nsteps = x + ndx, y + ndy, 0
            while 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] in [0, '2']:
                if maze[nx][ny] == '2':
                    nx, ny = portal_dict[(nx, ny)]
                nx += ndx
                ny += ndy
                nsteps += 1
            nx -= ndx
            ny -= ndy

            if not(0 <= nx < rows and 0 <= ny < cols) or distances[(nx, ny, ndx, ndy)] <= current_dist + nsteps:
                continue
            distances[(nx, ny, ndx, ndy)] = current_dist + nsteps
            heappush(heap, (distances[(nx, ny, ndx, ndy)], (nx, ny, ndx, ndy)))

    return -1