"""
QUESTION:
Write a function `find_directions(labyrinth, robot, station)` that takes a 2D grid `labyrinth` where 0 represents an empty space and 1 represents a wall, a list `robot` representing the robot's position, and a list `station` representing the charging station's position. The function should return a string of directions (`'u'`, `'d'`, `'l'`, `'r'`) that the robot should follow to reach the charging station with the least number of moves possible. If there are multiple valid directions, return the lexicographically minimum one. If the robot can't reach the charging station, return `"no way"`. 

Constraints: 
- `labyrinth` is an `m x n` grid where `1 <= m, n <= 100` and `labyrinth[i][j]` is either `0` or `1`.
- `robot` and `station` are lists of length 2 representing the row and column of the robot and the charging station respectively.
- The robot and the charging station are in empty spaces and are not at the same position initially.
"""

from collections import deque

def find_directions(labyrinth, robot, station):
    rows, cols = len(labyrinth), len(labyrinth[0])
    robot_row, robot_col = robot
    station_row, station_col = station
    visited = [[False]*cols for _ in range(rows)]
    parent = [[None]*cols for _ in range(rows)]
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    direction = ['u', 'r', 'd', 'l']

    queue = deque([(robot_row, robot_col)])
    visited[robot_row][robot_col] = True

    while queue:
        x, y = queue.popleft()

        if (x, y) == (station_row, station_col):
            path = []
            while parent[x][y]:
                nx, ny, d = parent[x][y]
                path.append(d)
                x, y = nx, ny
            return ''.join(path[::-1])

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and labyrinth[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = True
                parent[nx][ny] = (x, y, direction[i])

    return "no way"