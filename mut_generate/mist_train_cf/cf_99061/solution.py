"""
QUESTION:
Implement the `astar` function to generate an optimal path from a robot's starting position to a goal position in a 2D grid map with obstacles. The function should take into account the grid map representation and the movement costs in different directions. The grid map should be represented as a 2D list of boolean values, where `True` represents an obstacle and `False` represents a free space. The function should return a list of coordinates representing the shortest path from the start to the goal.

The movement costs are defined as follows: moving straight (horizontally or vertically) costs 10 units, and moving diagonally costs 14 units. The heuristic function should be used to estimate the cost from a given position to the goal.

Restrictions:

* The start and goal positions are represented as tuples of two integers.
* The grid map is a 2D list of boolean values.
* The function should return `None` if no path is found.
* The function should use a priority queue to efficiently explore the grid map.
"""

import heapq

MOVE_COST_STRAIGHT = 10
MOVE_COST_DIAGONAL = 14

def heuristic(position, goal):
    dx = abs(position[0] - goal[0])
    dy = abs(position[1] - goal[1])
    return MOVE_COST_STRAIGHT * (dx + dy) + (MOVE_COST_DIAGONAL - 2 * MOVE_COST_STRAIGHT) * min(dx, dy)

def astar(start, goal, grid_map):
    open_set = []
    closed_set = set()
    heapq.heappush(open_set, (0, start))
    g_scores = {start: 0}
    f_scores = {start: heuristic(start, goal)}
    came_from = {start: None}

    while open_set:
        current = heapq.heappop(open_set)[1]
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        closed_set.add(current)
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if not (0 <= neighbor[0] < len(grid_map) and 0 <= neighbor[1] < len(grid_map[0])) or grid_map[neighbor[0]][neighbor[1]]:
                continue
            tentative_g_score = g_scores[current] + (MOVE_COST_STRAIGHT if dx == 0 or dy == 0 else MOVE_COST_DIAGONAL)
            if neighbor in closed_set and tentative_g_score >= g_scores.get(neighbor, float('inf')):
                continue
            if tentative_g_score < g_scores.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_scores[neighbor] = tentative_g_score
                f_scores[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_scores[neighbor], neighbor))
    return None