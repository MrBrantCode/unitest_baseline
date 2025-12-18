"""
QUESTION:
Given a total number of courses `n` and an array of prerequisite relationships `relations`, where `relations[i] = [a, b]` represents course `a` must be completed before course `b`, determine the least number of semesters required to complete all courses. If it's impossible to complete all courses due to a cycle, return `-1`. 

The constraints are `1 <= n <= 5000`, `1 <= relations.length <= 5000`, `1 <= a, b <= n`, `a != b`, and all pairs `[a, b]` are distinct. 

Implement a function `minSemesters(n, relations)` that returns the least number of semesters required to complete all courses or `-1` if it's impossible.
"""

from collections import defaultdict, deque

def minSemesters(n, relations):
    graph = defaultdict(list)
    in_degree = {i: 0 for i in range(1, n+1)}

    for a, b in relations:
        graph[a].append(b)
        in_degree[b] += 1

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    depth = {node: 1 for node in queue}
    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                depth[nei] = depth[node] + 1
                queue.append(nei)

    if len(depth) == n:
        return max(depth.values())
    else:
        return -1