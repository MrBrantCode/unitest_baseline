"""
QUESTION:
Create a function named `a_star_search` that implements the A* search algorithm for pathfinding and graph traversal. The function should take in a graph, a start node, a goal node, and a heuristic function. It should return the shortest path from the start node to the goal node if one exists, or a failure signal if no path exists. The function should use two lists: `openList` to keep track of nodes to be evaluated and `closedList` to keep track of evaluated nodes. It should also use two dictionaries: `gScores` to store the cost to reach each node from the start node and `fScores` to store the estimated total cost to reach the goal node from each node.
"""

import heapq

def a_star_search(graph, start, goal, heuristic):
    openList = []
    heapq.heappush(openList, (0, start))
    closedList = set()
    gScores = {start: 0}
    fScores = {start: heuristic(start, goal)}
    cameFrom = {start: None}

    while openList:
        _, currentNode = heapq.heappop(openList)

        if currentNode == goal:
            return reconstruct_path(cameFrom, currentNode)

        closedList.add(currentNode)

        for neighbor, weight in graph[currentNode].items():
            if neighbor in closedList:
                continue
            if neighbor not in gScores or gScores[currentNode] + weight < gScores[neighbor]:
                gScores[neighbor] = gScores[currentNode] + weight
                fScores[neighbor] = gScores[neighbor] + heuristic(neighbor, goal)
                cameFrom[neighbor] = currentNode
                heapq.heappush(openList, (fScores[neighbor], neighbor))

    return None

def reconstruct_path(cameFrom, current):
    total_path = [current]
    while cameFrom[current] is not None:
        current = cameFrom[current]
        total_path.insert(0, current)
    return total_path