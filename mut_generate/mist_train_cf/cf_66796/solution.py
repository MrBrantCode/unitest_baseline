"""
QUESTION:
Write a function `minDistance` that calculates the minimal distance for a squirrel to collect all the nuts and put them under a tree one by one in a grid with obstacles. The function takes four parameters: `height` and `width` of the grid, `tree` position, `squirrel` position, `nuts` positions, and `obstacles` positions. The squirrel can only take at most one nut at a time and can move in four directions - up, down, left, and right, to the adjacent cell. The given positions of nuts have no order, and the squirrel cannot pass through the obstacles. The function should return the minimal distance as an integer. The grid size is restricted to 3 <= height * width <= 10,000.
"""

import heapq

def minDistance(height, width, tree, squirrel, nuts, obstacles):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def astar(start, goal, avoid=None):
        queue = [(0, start)]
        visited = set()
        while queue:
            cost, pos = heapq.heappop(queue)
            if pos == goal:
                return cost
            if pos in visited:
                continue
            visited.add(pos)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = pos[0] + dx, pos[1] + dy
                if (0 <= x < height and 0 <= y < width and 
                    (x, y) not in obstacles and (x, y) != avoid):
                    heapq.heappush(queue, (cost + 1 + heuristic((x, y), goal), (x, y)))
        return float('inf')

    total_distance = sum(heuristic(nut, tree) for nut in nuts)
    for nut in nuts:
        distance = astar(squirrel, nut) + astar(nut, tree, avoid=squirrel)
        if distance == float('inf'):
            return -1
        total_distance += distance - heuristic(nut, tree)
    return total_distance