"""
QUESTION:
Alice got tired of playing the tag game by the usual rules so she offered Bob a little modification to it. Now the game should be played on an undirected rooted tree of n vertices. Vertex 1 is the root of the tree.

Alice starts at vertex 1 and Bob starts at vertex x (x ≠ 1). The moves are made in turns, Bob goes first. In one move one can either stay at the current vertex or travel to the neighbouring one.

The game ends when Alice goes to the same vertex where Bob is standing. Alice wants to minimize the total number of moves and Bob wants to maximize it.

You should write a program which will determine how many moves will the game last.


-----Input-----

The first line contains two integer numbers n and x (2 ≤ n ≤ 2·10^5, 2 ≤ x ≤ n).

Each of the next n - 1 lines contains two integer numbers a and b (1 ≤ a, b ≤ n) — edges of the tree. It is guaranteed that the edges form a valid tree.


-----Output-----

Print the total number of moves Alice and Bob will make.


-----Examples-----
Input
4 3
1 2
2 3
2 4

Output
4

Input
5 2
1 2
2 3
3 4
2 5

Output
6



-----Note-----

In the first example the tree looks like this:

 [Image] 

The red vertex is Alice's starting position, the blue one is Bob's. Bob will make the game run the longest by standing at the vertex 3 during all the game. So here are the moves:

B: stay at vertex 3

A: go to vertex 2

B: stay at vertex 3

A: go to vertex 3

In the second example the tree looks like this:

 [Image] 

The moves in the optimal strategy are:

B: go to vertex 3

A: go to vertex 2

B: go to vertex 4

A: go to vertex 3

B: stay at vertex 4

A: go to vertex 4
"""

from collections import deque

def calculate_game_moves(n, x, edges):
    # Initialize adjacency list
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Initialize distance and parent arrays
    dist = [0] * (n + 1)
    parent = [0] * (n + 1)
    visited = [0] * (n + 1)
    dist2 = [0] * (n + 1)
    visited2 = [0] * (n + 1)
    
    # Perform BFS from the root (vertex 1)
    s = deque([1])
    while s:
        curr = s[-1]
        if not visited[curr]:
            visited[curr] = 1
            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    parent[neighbor] = curr
                    s.append(neighbor)
                    dist[neighbor] = dist[curr] + 1
        else:
            s.pop()
    
    # Move Bob up the tree to a strategic position
    curr = x
    moved_up = 0
    while moved_up + 1 < dist[parent[curr]]:
        curr = parent[curr]
        moved_up += 1
    
    # Perform BFS from Bob's strategic position
    s = deque([curr])
    while s:
        curr = s[-1]
        if not visited2[curr]:
            visited2[curr] = 1
            for neighbor in adj[curr]:
                if parent[curr] != neighbor:
                    s.append(neighbor)
                    dist2[neighbor] = dist2[curr] + 1
        else:
            s.pop()
    
    # Find the best location for Bob to maximize the game duration
    best_loc = 0
    best_dist = -1
    for i in range(n + 1):
        if visited2[i] and dist2[i] > best_dist:
            best_dist = dist2[i]
            best_loc = i
    
    # Return the total number of moves
    return 2 * dist[best_loc]