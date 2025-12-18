"""
QUESTION:
Write a function `distance_between_nodes(tree, root, node1, node2)` that takes in a 2D matrix `tree` representing a tree, and three integers `root`, `node1`, and `node2`, where `tree[i][j]` is 1 if there is an edge between nodes `i` and `j`, and 0 otherwise. The function should return an integer representing the distance between `node1` and `node2` in the given tree, defined as the number of edges on the path between the nodes, given that `1 <= len(tree) <= 1000` and `0 <= root, node1, node2 < len(tree)`.
"""

from collections import deque

def distance_between_nodes(tree, root, node1, node2):
    def find_path_length(tree, start, end):
        visited = [False] * len(tree)
        queue = deque([(start, 0)])
        while queue:
            current, distance = queue.popleft()
            if current == end:
                return distance
            visited[current] = True
            for neighbor, connected in enumerate(tree[current]):
                if connected and not visited[neighbor]:
                    queue.append((neighbor, distance + 1))
        return -1  # If no path found

    return find_path_length(tree, node1, root) + find_path_length(tree, node2, root)