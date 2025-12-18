"""
QUESTION:
In Absurdistan, there are n towns (numbered 1 through n) and m bidirectional railways. There is also an absurdly simple road network — for each pair of different towns x and y, there is a bidirectional road between towns x and y if and only if there is no railway between them. Travelling to a different town using one railway or one road always takes exactly one hour.

A train and a bus leave town 1 at the same time. They both have the same destination, town n, and don't make any stops on the way (but they can wait in town n). The train can move only along railways and the bus can move only along roads.

You've been asked to plan out routes for the vehicles; each route can use any road/railway multiple times. One of the most important aspects to consider is safety — in order to avoid accidents at railway crossings, the train and the bus must not arrive at the same town (except town n) simultaneously.

Under these constraints, what is the minimum number of hours needed for both vehicles to reach town n (the maximum of arrival times of the bus and the train)? Note, that bus and train are not required to arrive to the town n at the same moment of time, but are allowed to do so.

Input

The first line of the input contains two integers n and m (2 ≤ n ≤ 400, 0 ≤ m ≤ n(n - 1) / 2) — the number of towns and the number of railways respectively.

Each of the next m lines contains two integers u and v, denoting a railway between towns u and v (1 ≤ u, v ≤ n, u ≠ v).

You may assume that there is at most one railway connecting any two towns.

Output

Output one integer — the smallest possible time of the later vehicle's arrival in town n. If it's impossible for at least one of the vehicles to reach town n, output  - 1.

Examples

Input

4 2
1 3
3 4


Output

2


Input

4 6
1 2
1 3
1 4
2 3
2 4
3 4


Output

-1


Input

5 5
4 2
3 5
4 5
5 1
1 2


Output

3

Note

In the first sample, the train can take the route <image> and the bus can take the route <image>. Note that they can arrive at town 4 at the same time.

In the second sample, Absurdistan is ruled by railwaymen. There are no roads, so there's no way for the bus to reach town 4.
"""

def minimum_travel_time(n, m, railways):
    # Initialize distance matrix
    dist = [[1] * (n + 1) for _ in range(n + 1)]
    
    # Set distances for railways
    for a, b in railways:
        dist[a][b] = dist[b][a] = 2
    
    # Determine the type of transportation (1 for road, 2 for railway)
    x = 3 - dist[1][n]
    
    # Initialize visited array and distance array
    visited = [0] * (n + 1)
    d = [n + 1] * (n + 1)
    d[1] = 0
    
    # Perform BFS
    i = 1
    while i != n:
        visited[i] = 1
        for j in range(1, n + 1):
            if visited[j] == 0 and dist[i][j] == x and d[j] > d[i] + 1:
                d[j] = d[i] + 1
        
        # Find the next unvisited town with the minimum distance
        meu = n + 1
        for j in range(1, n + 1):
            if visited[j] == 0 and d[j] < meu:
                meu = d[j]
                i = j
        
        # If no valid town is found, return -1
        if meu == n + 1:
            return -1
        elif i == n:
            return d[n]
    
    return d[n]