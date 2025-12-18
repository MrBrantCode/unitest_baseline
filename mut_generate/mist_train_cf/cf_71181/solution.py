"""
QUESTION:
Write a function `shortestDistance` that takes in four parameters: a 2D list `maze` representing a maze with empty spaces (0), walls (1), and portals (2), a list `start` representing the start position, a list `destination` representing the destination position, and a 2D list `portals` representing the positions of the two portals. The function should return the shortest distance for the ball to stop at the destination. If the ball cannot stop at the destination, return -1. The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). Traveling through a portal counts as 1 distance. The maze's borders are all walls and the ball can go through the empty spaces by rolling up, down, left, or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. If the ball hits a portal, it will be transported to the other portal. 

Constraints: 
- `m == maze.length`
- `n == maze[i].length`
- `1 <= m, n <= 100`
- `maze[i][j]` is `0`, `1`, or `2`.
- `start.length == 2`
- `destination.length == 2`
- `portals.length == 2`
- `0 <= startrow, destinationrow, portal1row, portal2row <= m`
- `0 <= startcol, destinationcol, portal1col, portal2col <= n`
- Both the ball and the destination exist in an empty space, and they will not be in the same position initially.
- The maze contains at least 2 empty spaces and 2 portals.
"""

from collections import deque

def shortestDistance(maze, start, destination, portals):
    directions = [(0,1),(0,-1),(1,0),(-1,0)]  # right, left, down, up
    queue = deque([(start, 0)])  # position and distance
    visited = {tuple(start): 0}
    portal_dict = {tuple(portals[0]): portals[1], tuple(portals[1]): portals[0]}

    while queue:
        position, dist = queue.popleft()
        for d in directions:
            x, y, tmp = position[0], position[1], 0
            while 0<=x+d[0]<len(maze) and 0<=y+d[1]<len(maze[0]) and maze[x+d[0]][y+d[1]]!=1:   # while it can roll
                x += d[0]
                y += d[1]
                tmp += 1    # the distance increases
                if maze[x][y]==2:   # a portal
                    x, y = portal_dict[(x, y)]
                    tmp += 1   # teleport counts additional 1 distance
                    break
            if (x, y) not in visited or dist+tmp<visited[(x, y)]:  # if it's a new position or we find a shorter path
                visited[(x, y)] = dist+tmp
                if (x, y)!=tuple(destination):   # if new position is not the destination, add it to the queue
                    queue.append(((x, y), dist+tmp))

    if tuple(destination) in visited:   # if the destination is reached
        return visited[tuple(destination)]
    else:   # if the destination is unreachable
        return -1