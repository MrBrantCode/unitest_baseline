"""
QUESTION:
Tomya is a girl. She loves Chef Ciel very much.

Today, too, Tomya is going to Ciel's restaurant.
Of course, Tomya would like to go to Ciel's restaurant as soon as possible.
Therefore Tomya uses one of the shortest paths from Tomya's house to Ciel's restaurant.
On the other hand, Tomya is boring now to use the same path many times.
So Tomya wants to know the number of shortest paths from Tomya's house to Ciel's restaurant.
Your task is to calculate the number under the following assumptions.

This town has N intersections and M two way roads.
The i-th road connects from the Ai-th intersection to the Bi-th intersection, and its length is 

Ci.
Tomya's house is in the 1st intersection, and Ciel's restaurant is in the N-th intersection.

-----Input-----

The first line contains an integer T, the number of test cases.
Then T test cases follow.
The first line of each test case contains 2 integers N, M.
Then next M lines contains 3 integers denoting Ai, Bi and Ci.

-----Output-----

For each test case, print the number of shortest paths from Tomya's house to Ciel's restaurant.

-----Constraints-----

1 ≤ T ≤ 10

2 ≤ N ≤ 10

1 ≤ M ≤ N ∙ (N – 1) / 2

1 ≤ Ai, Bi ≤ N

1 ≤ Ci ≤ 10
Ai ≠ Bi

If i ≠ j and Ai = Aj, then Bi ≠ Bj

There is at least one path from Tomya's house to Ciel's restaurant.

-----Sample Input-----
2
3 3
1 2 3
2 3 6
1 3 7
3 3
1 2 3
2 3 6
1 3 9

-----Sample Output-----
1
2

-----Explanations-----

In the first sample, only one shortest path exists, which is 1-3.

In the second sample, both paths 1-2-3 and 1-3 are the shortest paths.
"""

def count_shortest_paths(N, M, roads):
    # Initialize the graph
    g = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    
    # Populate the graph with road information
    for (Ai, Bi, Ci) in roads:
        g[Ai][Bi] = Ci
        g[Bi][Ai] = Ci
    
    # List to store the distances of the shortest paths
    x = []
    
    # Distance array initialized to -1 (indicating unvisited nodes)
    d = [-1] * (N + 1)
    d[1] = 0  # Starting point distance is 0
    
    # Recursive function to explore all paths
    def snek(k, n, x, d, g):
        if k == n:
            x.append(d[n])
            return
        for i in range(1, n + 1):
            if g[k][i] != 0 and d[i] == -1:
                d[i] = d[k] + g[k][i]
                snek(i, n, x, d, g)
                d[i] = -1
    
    # Start the recursive exploration from the 1st intersection
    snek(1, N, x, d, g)
    
    # Sort the distances to find the shortest paths
    x.sort()
    
    # The shortest distance
    r = x[0]
    
    # Count the number of shortest paths
    ans = 0
    for z in range(len(x)):
        if r == x[z]:
            ans += 1
    
    return ans