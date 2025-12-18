"""
QUESTION:
You are given a rooted tree with root in vertex 1. Each vertex is coloured in some colour.

Let's call colour c dominating in the subtree of vertex v if there are no other colours that appear in the subtree of vertex v more times than colour c. So it's possible that two or more colours will be dominating in the subtree of some vertex.

The subtree of vertex v is the vertex v and all other vertices that contains vertex v in each path to the root.

For each vertex v find the sum of all dominating colours in the subtree of vertex v.


-----Input-----

The first line contains integer n (1 ≤ n ≤ 10^5) — the number of vertices in the tree.

The second line contains n integers c_{i} (1 ≤ c_{i} ≤ n), c_{i} — the colour of the i-th vertex.

Each of the next n - 1 lines contains two integers x_{j}, y_{j} (1 ≤ x_{j}, y_{j} ≤ n) — the edge of the tree. The first vertex is the root of the tree.


-----Output-----

Print n integers — the sums of dominating colours for each vertex.


-----Examples-----
Input
4
1 2 3 4
1 2
2 3
2 4

Output
10 9 3 4

Input
15
1 2 3 1 2 3 3 1 1 3 2 2 1 2 3
1 2
1 3
1 4
1 14
1 15
2 5
2 6
2 7
3 8
3 9
3 10
4 11
4 12
4 13

Output
6 5 4 3 2 3 3 1 1 3 2 2 1 2 3
"""

from collections import defaultdict

class SumDefaultdict(defaultdict):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(int, *args, **kwargs)
        self.mx = max(self.values())
        self.mx_sum = sum((c for (c, v) in self.items() if v == self.mx))

    def sumadd(self, map):
        for (bb, val) in map.items():
            if val > 0:
                self[bb] += val
                if self[bb] > self.mx:
                    self.mx = self[bb]
                    self.mx_sum = bb
                elif self[bb] == self.mx:
                    self.mx_sum += bb

def calculate_dominating_colours_sum(n, colours, edges):
    # Initialize the adjacency list for the tree
    adjacency_list = [[] for _ in range(n)]
    for (a, b) in edges:
        adjacency_list[a - 1].append(b - 1)
        adjacency_list[b - 1].append(a - 1)
    
    # Perform a BFS to determine the depth and parent of each node
    depth = [0] + [None] * (n - 1)
    parent = [None] * n
    que = [0]
    index = 0
    while index < len(que):
        curr = que[index]
        for b in adjacency_list[curr]:
            if depth[b] is None:
                depth[b] = depth[curr] + 1
                parent[b] = curr
                que.append(b)
        index += 1
    
    # Sort vertices by depth in descending order
    order = sorted(((depth[i], i) for i in range(n)), reverse=True)
    
    # Initialize the colour counts for each vertex
    cols = [SumDefaultdict({colours[i]: 1}) for i in range(n)]
    
    # Calculate the sum of dominating colours for each vertex
    answer = [0] * n
    for (d, i) in order:
        children = sorted([cols[b] for b in adjacency_list[i] if depth[b] > d], key=len, reverse=True)
        if children:
            for j in range(1, len(children)):
                children[0].sumadd(children[j])
            children[0].sumadd({colours[i]: 1})
            cols[i] = children[0]
        answer[i] = cols[i].mx_sum
    
    return answer