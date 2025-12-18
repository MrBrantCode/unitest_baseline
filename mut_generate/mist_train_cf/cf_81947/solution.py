"""
QUESTION:
Write a function `shortestAlternatingPaths(n, red_edges, blue_edges)` that takes as input an integer `n`, a list of red edges `red_edges`, and a list of blue edges `blue_edges` of a directed graph, where each edge is represented as a list `[i, j, w]` denoting a directed edge from node `i` to node `j` with weight `w`. Return an array `answer` of length `n`, where each `answer[X]` is the length of the shortest path from node `0` to node `X` such that the edge colors alternate along the path and the total weight of the path is minimized (or `-1` if such a path doesn't exist). The constraints are `1 <= n <= 100`, `red_edges.length <= 400`, `blue_edges.length <= 400`, `0 <= red_edges[i][j], blue_edges[i][j] < n`, and `1 <= red_edges[i][2], blue_edges[i][2] <= 100`.
"""

from collections import defaultdict, deque
def shortestAlternatingPaths(n, red_edges, blue_edges):
    red = defaultdict(list)
    blue = defaultdict(list)
    for i, j, w in red_edges:
        red[i].append((j, w))
    for i, j, w in blue_edges:
        blue[i].append((j, w))

    result = [[-1,-1] for _ in range(n)]
    result[0] = [0,0]

    queue = deque([(0, True), (0, False)])  
    while queue:
        node, is_red = queue.popleft()
        if is_red:
            for next_node, weight in red[node]:
                if result[next_node][0] == -1 or result[node][0] + weight < result[next_node][0]:
                    result[next_node][0] = result[node][0] + weight
                    queue.append((next_node, False))
        else:
            for next_node, weight in blue[node]:
                if result[next_node][1] == -1 or result[node][1] + weight < result[next_node][1]:
                    result[next_node][1] = result[node][1] + weight
                    queue.append((next_node, True))

    return [x if y == -1 else y if x == -1 else min(x, y) for x, y in result]