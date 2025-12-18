"""
QUESTION:
Takahashi and Aoki will play a game on a tree. The tree has N vertices numbered 1 to N, and the i-th of the N-1 edges connects Vertex a_i and Vertex b_i.

At the beginning of the game, each vertex contains a coin. Starting from Takahashi, he and Aoki will alternately perform the following operation:

* Choose a vertex v that contains one or more coins, and remove all the coins from v.
* Then, move each coin remaining on the tree to the vertex that is nearest to v among the adjacent vertices of the coin's current vertex.



The player who becomes unable to play, loses the game. That is, the player who takes his turn when there is no coin remaining on the tree, loses the game. Determine the winner of the game when both players play optimally.

Constraints

* 1 \leq N \leq 2 \times 10^5
* 1 \leq a_i, b_i \leq N
* a_i \neq b_i
* The graph given as input is a tree.

Input

Input is given from Standard Input in the following format:


N
a_1 b_1
a_2 b_2
:
a_{N-1} b_{N-1}


Output

Print `First` if Takahashi will win, and print `Second` if Aoki will win.

Examples

Input

3
1 2
2 3


Output

First


Input

6
1 2
2 3
2 4
4 6
5 6


Output

Second


Input

7
1 7
7 4
3 4
7 5
6 3
2 1


Output

First
"""

import sys
from collections import deque

def determine_winner(N, edges):
    # Create the graph as an adjacency list
    graph = [[] for _ in range(N)]
    for (a, b) in edges:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    def bfs(node):
        searched = [False] * N
        que = deque([(node, 0)])
        (v, dist) = (0, 0)
        while que:
            (v, dist) = que.popleft()
            searched[v] = True
            for child in graph[v]:
                if not searched[child]:
                    que.append((child, dist + 1))
        return (v, dist)

    # Find the farthest node from any starting node (0 in this case)
    (e, _) = bfs(0)
    # Find the diameter of the tree by finding the farthest node from 'e'
    (_, diameter) = bfs(e)
    
    # Determine the winner based on the diameter
    return 'Second' if diameter % 3 == 1 else 'First'