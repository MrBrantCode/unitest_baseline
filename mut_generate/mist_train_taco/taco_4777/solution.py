"""
QUESTION:
Little town Nsk consists of n junctions connected by m bidirectional roads. Each road connects two distinct junctions and no two roads connect the same pair of junctions. It is possible to get from any junction to any other junction by these roads. The distance between two junctions is equal to the minimum possible number of roads on a path between them.

In order to improve the transportation system, the city council asks mayor to build one new road. The problem is that the mayor has just bought a wonderful new car and he really enjoys a ride from his home, located near junction s to work located near junction t. Thus, he wants to build a new road in such a way that the distance between these two junctions won't decrease. 

You are assigned a task to compute the number of pairs of junctions that are not connected by the road, such that if the new road between these two junctions is built the distance between s and t won't decrease.


-----Input-----

The firt line of the input contains integers n, m, s and t (2 ≤ n ≤ 1000, 1 ≤ m ≤ 1000, 1 ≤ s, t ≤ n, s ≠ t) — the number of junctions and the number of roads in Nsk, as well as the indices of junctions where mayors home and work are located respectively. The i-th of the following m lines contains two integers u_{i} and v_{i} (1 ≤ u_{i}, v_{i} ≤ n, u_{i} ≠ v_{i}), meaning that this road connects junctions u_{i} and v_{i} directly. It is guaranteed that there is a path between any two junctions and no two roads connect the same pair of junctions.


-----Output-----

Print one integer — the number of pairs of junctions not connected by a direct road, such that building a road between these two junctions won't decrease the distance between junctions s and t.


-----Examples-----
Input
5 4 1 5
1 2
2 3
3 4
4 5

Output
0

Input
5 4 3 5
1 2
2 3
3 4
4 5

Output
5

Input
5 6 1 5
1 2
1 3
1 4
4 5
3 5
2 5

Output
3
"""

def count_valid_road_pairs(n, m, s, t, roads):
    from collections import deque

    # Convert 1-based indices to 0-based
    s -= 1
    t -= 1

    # Create adjacency list for the graph
    adj = [[] for _ in range(n)]
    for u, v in roads:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)

    # Function to perform BFS and compute distances from a start node
    def bfs(start):
        distances = [-1] * n
        distances[start] = 0
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[node] + 1
                    queue.append(neighbor)
        return distances

    # Compute distances from s and t
    dist_from_s = bfs(s)
    dist_from_t = bfs(t)
    distance_st = dist_from_s[t]

    # Count valid pairs
    valid_pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            if j not in adj[i]:
                if dist_from_s[i] + 1 + dist_from_t[j] >= distance_st and \
                   dist_from_t[i] + 1 + dist_from_s[j] >= distance_st:
                    valid_pairs += 1

    return valid_pairs