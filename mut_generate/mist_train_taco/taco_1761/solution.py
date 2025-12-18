"""
QUESTION:
The country Treeland consists of n cities, some pairs of them are connected with unidirectional roads. Overall there are n - 1 roads in the country. We know that if we don't take the direction of the roads into consideration, we can get from any city to any other one.

The council of the elders has recently decided to choose the capital of Treeland. Of course it should be a city of this country. The council is supposed to meet in the capital and regularly move from the capital to other cities (at this stage nobody is thinking about getting back to the capital from these cities). For that reason if city a is chosen a capital, then all roads must be oriented so that if we move along them, we can get from city a to any other city. For that some roads may have to be inversed.

Help the elders to choose the capital so that they have to inverse the minimum number of roads in the country.

Input

The first input line contains integer n (2 ≤ n ≤ 2·105) — the number of cities in Treeland. Next n - 1 lines contain the descriptions of the roads, one road per line. A road is described by a pair of integers si, ti (1 ≤ si, ti ≤ n; si ≠ ti) — the numbers of cities, connected by that road. The i-th road is oriented from city si to city ti. You can consider cities in Treeland indexed from 1 to n.

Output

In the first line print the minimum number of roads to be inversed if the capital is chosen optimally. In the second line print all possible ways to choose the capital — a sequence of indexes of cities in the increasing order.

Examples

Input

3
2 1
2 3


Output

0
2 


Input

4
1 4
2 4
3 4


Output

2
1 2 3
"""

import sys
from collections import defaultdict

def find_optimal_capital(n, roads):
    class Graph:
        def __init__(self, n):
            self.graph = {i: [] for i in range(1, n + 1)}
            self.distance = [0] * (n + 1)
            self.distance[0] = sys.maxsize
            self.min_dist = sys.maxsize
            self.summation = n * (n + 1) // 2

        def dfs(self, root, visited=defaultdict(bool)):
            stack, path = [root], []
            rev = 0
            visited[root] = True
            while stack:
                s = stack.pop()
                visited[s] = True
                for v in self.graph[s]:
                    if v[0] not in visited:
                        dist = self.distance[s] + v[1]
                        if dist < self.min_dist:
                            self.min_dist = dist
                        self.distance[v[0]] = dist
                        self.summation -= v[0]
                        if v[1] == -1:
                            rev += 1
                        path.append(s)
                        stack.append(v[0])
            return rev

        def get_min_distance(self):
            return min(self.distance)

    g = Graph(n)
    for (x, y) in roads:
        g.graph[x].append([y, 1])
        g.graph[y].append([x, -1])

    total_rev = g.dfs(1)
    min_distance = 0 if g.summation > 0 and g.min_dist > 0 else g.min_dist
    optimal_capitals = [i for i in range(1, n + 1) if g.distance[i] == min_distance]

    return total_rev + min_distance, optimal_capitals