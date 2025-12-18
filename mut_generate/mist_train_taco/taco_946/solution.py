"""
QUESTION:
Monk visits the land of Islands.  There are a total of N islands numbered from 1 to N.  Some pairs of islands are connected to each other by Bidirectional bridges running over water.
Monk hates to cross these bridges as they require a lot of efforts. He is standing at Island #1 and wants to reach the Island #N. Find the minimum the number of bridges that he shall have to cross, if he takes the optimal route.   

Input:
First line contains T. T testcases follow.
First line of each test case contains two space-separated integers N, M.
Each of the next M lines contains two space-separated integers X and Y , denoting that there is a bridge between Island X and Island Y.  

Output:
Print the answer to each test case in a new line.

Constraints:
1 ≤ T ≤ 10
1 ≤ N ≤ 10^4
1 ≤ M ≤ 10^5
1 ≤ X, Y ≤ N

SAMPLE INPUT
2
3 2
1 2
2 3
4 4
1 2
2 3
3 4
4 2

SAMPLE OUTPUT
2
2
"""

from collections import deque

def find_min_bridges(N, M, bridges):
    # Initialize visited and level arrays
    visited = [False] * (N + 1)
    level = [0] * (N + 1)
    
    # Build the graph
    graph = {i: [] for i in range(1, N + 1)}
    for x, y in bridges:
        graph[x].append(y)
        graph[y].append(x)
    
    # BFS function to find the level of each node
    def bfs(graph, start):
        q = deque([start])
        visited[start] = True
        while q:
            p = q.popleft()
            for neighbor in graph[p]:
                if not visited[neighbor]:
                    level[neighbor] = level[p] + 1
                    q.append(neighbor)
                    visited[neighbor] = True
    
    # Perform BFS starting from Island #1
    bfs(graph, 1)
    
    # Return the level of Island #N
    return level[N]