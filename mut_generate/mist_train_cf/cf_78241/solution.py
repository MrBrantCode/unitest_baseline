"""
QUESTION:
Design a function called `is_network_fault_tolerant` that determines whether a given network is fault-tolerant, i.e., whether it can sustain data transmission perpetually even if some connections fail. The network is represented as an adjacency matrix where rows and columns represent routers and a 1 indicates a direct connection between those routers. The function should return True if the network is fault-tolerant and False otherwise.
"""

from collections import deque

def is_network_fault_tolerant(network):
    n = len(network)
    visited = [False] * n

    # BFS
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            for i in range(n):
                if network[node][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

    # Check if all nodes are connected
    bfs(0)
    if not all(visited):
        return False

    # Check if the network remains connected after removing each edge
    for i in range(n):
        for j in range(n):
            if network[i][j] == 1:
                network[i][j] = network[j][i] = 0
                visited = [False] * n
                bfs(0)
                if not all(visited):
                    return False
                network[i][j] = network[j][i] = 1

    return True