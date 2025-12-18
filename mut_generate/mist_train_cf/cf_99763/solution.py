"""
QUESTION:
Implement a motion planning algorithm using the A* algorithm to generate an optimal path from a robot's starting position to a goal position in a 2D grid map environment, considering any obstacles. Define a function `astar(start, goal, grid_map)` where `start` is the starting position, `goal` is the goal position, and `grid_map` is a 2D grid map where 0 represents an empty space and 1 represents an obstacle. The function should return the shortest path from the start to the goal as a list of positions, or `None` if no path is found.
"""

import heapq

# Define the cost of moving in different directions
MOVE_COST_STRAIGHT = 10
MOVE_COST_DIAGONAL = 14

# Define the heuristic function for A*
def heuristic(position, goal):
    dx = abs(position[0] - goal[0])
    dy = abs(position[1] - goal[1])
    return MOVE_COST_STRAIGHT * (dx + dy) + (MOVE_COST_DIAGONAL - 2 * MOVE_COST_STRAIGHT) * min(dx, dy)

# Define the A* algorithm for pathfinding
def astar(start, goal, grid_map):
    # Initialize the open and closed sets
    open_set = []
    closed_set = set()
    # Add the start position to the open set
    heapq.heappush(open_set, (0, start))
    # Initialize the g and f scores for each position
    g_scores = {start: 0}
    f_scores = {start: heuristic(start, goal)}
    came_from = {}
    # Loop until the open set is empty
    while open_set:
        # Get the position with the lowest f score from the open set
        current = heapq.heappop(open_set)[1]
        # Check if the current position is the goal
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        # Add the current position to the closed set
        closed_set.add(current)
        # Loop through the neighboring positions
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            # Check if the neighbor is outside the grid map or is an obstacle
            if not (0 <= neighbor[0] < len(grid_map) and 0 <= neighbor[1] < len(grid_map[0])) or grid_map[neighbor[0]][neighbor[1]]:
                continue
            # Calculate the tentative g score for the neighbor
            tentative_g_score = g_scores[current] + (MOVE_COST_STRAIGHT if dx == 0 or dy == 0 else MOVE_COST_DIAGONAL)
            # Check if the neighbor is already in the closed set or has a better g score
            if neighbor in closed_set and tentative_g_score >= g_scores.get(neighbor, float('inf')):
                continue
            # Add the neighbor to the open set and update its g and f scores
            if tentative_g_score < g_scores.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_scores[neighbor] = tentative_g_score
                f_scores[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_scores[neighbor], neighbor))
    # No path found
    return None