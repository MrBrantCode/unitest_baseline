"""
QUESTION:
You are given a set of points `points` with integer coordinates `points[i] = [xi, yi]` and a set of obstacles `obstacles` with integer coordinates `obstacles[j] = [xj, yj]`. The function `minTimeToVisitAllPoints` should return the minimum time in seconds to visit all the points in the order given by `points` without passing through any obstacles. You can move according to these rules: 
- In 1 second, you can either move vertically by one unit, 
- move horizontally by one unit, or 
- move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second). 
You have to visit the points in the same order as they appear in the array. You are allowed to pass through points that appear later in the order, but these do not count as visits. You are not allowed to pass through any obstacles. 

Constraints:
- 1 <= n <= 100, where n is the number of points
- 0 <= m <= 100, where m is the number of obstacles
- -1000 <= xi, yi, xj, yj <= 1000
"""

def minTimeToVisitAllPoints(points, obstacles):
    time = 0
    obstacles_set = set((x, y) for x, y in obstacles)
    for i in range(len(points)-1):
        pt = points[i]
        next_pt = points[i+1]
        dx = abs(pt[0]-next_pt[0])
        dy = abs(pt[1]-next_pt[1])
        min_time = min(dx, dy) * (dx + dy - min(dx, dy)) ** 0.5 + abs(dx-dy)
        if dx == dy:
            min_time = dx
        time += min_time
        for x in range(min(pt[0], next_pt[0]), max(pt[0], next_pt[0])+1):
            for y in range(min(pt[1], next_pt[1]), max(pt[1], next_pt[1])+1):
                if (x, y) != pt and (x, y) != next_pt and (x, y) in obstacles_set:
                    time += 1
    return time