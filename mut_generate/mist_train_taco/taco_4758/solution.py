"""
QUESTION:
The Fair Nut is going to travel to the Tree Country, in which there are $n$ cities. Most of the land of this country is covered by forest. Furthermore, the local road system forms a tree (connected graph without cycles). Nut wants to rent a car in the city $u$ and go by a simple path to city $v$. He hasn't determined the path, so it's time to do it. Note that chosen path can consist of only one vertex.

A filling station is located in every city. Because of strange law, Nut can buy only $w_i$ liters of gasoline in the $i$-th city. We can assume, that he has infinite money. Each road has a length, and as soon as Nut drives through this road, the amount of gasoline decreases by length. Of course, Nut can't choose a path, which consists of roads, where he runs out of gasoline. He can buy gasoline in every visited city, even in the first and the last.

He also wants to find the maximum amount of gasoline that he can have at the end of the path. Help him: count it.


-----Input-----

The first line contains a single integer $n$ ($1 \leq n \leq 3 \cdot 10^5$) — the number of cities.

The second line contains $n$ integers $w_1, w_2, \ldots, w_n$ ($0 \leq w_{i} \leq 10^9$) — the maximum amounts of liters of gasoline that Nut can buy in cities.

Each of the next $n - 1$ lines describes road and contains three integers $u$, $v$, $c$ ($1 \leq u, v \leq n$, $1 \leq c \leq 10^9$, $u \ne v$), where $u$ and $v$ — cities that are connected by this road and $c$ — its length.

It is guaranteed that graph of road connectivity is a tree.


-----Output-----

Print one number — the maximum amount of gasoline that he can have at the end of the path.


-----Examples-----
Input
3
1 3 3
1 2 2
1 3 2

Output
3

Input
5
6 3 2 5 0
1 2 10
2 3 3
2 4 1
1 5 1

Output
7



-----Note-----

The optimal way in the first example is $2 \to 1 \to 3$.  [Image] 

The optimal way in the second example is $2 \to 4$.  [Image]
"""

def calculate_max_gasoline(n, w, roads):
    # Initialize the graph and other necessary data structures
    graph = [{} for _ in range(n)]
    for (u, v, c) in roads:
        u -= 1
        v -= 1
        if v in graph[u]:
            graph[u][v] = min(graph[u][v], c)
        else:
            graph[u][v] = c
        if u in graph[v]:
            graph[v][u] = min(graph[v][u], c)
        else:
            graph[v][u] = c
    
    gas = [{} for _ in range(n)]
    highs = [[0, 0] for _ in range(n)]
    path = [(0, 0)]
    ind = 0
    
    # Perform a DFS to build the path
    while ind < len(path):
        (cur, par) = path[ind]
        edges = graph[cur]
        for x in edges:
            if x != par:
                path.append((x, cur))
        ind += 1
    
    # Function to calculate the maximum gasoline for each node
    def mostGas(node, parent):
        edges = graph[node]
        high = w[node]
        high2 = w[node]
        for x in edges:
            if x != parent:
                gas[node][x] = highs[x][0] + w[node] - edges[x]
                if gas[node][x] > high:
                    (high, high2) = (gas[node][x], high)
                elif gas[node][x] > high2:
                    high2 = gas[node][x]
        highs[node] = [high, high2]
        return high
    
    # Calculate the maximum gasoline for each node in reverse order of the path
    for (x, y) in path[::-1]:
        mostGas(x, y)
    
    # Find the maximum gasoline that can be had at the end of the path
    high = 0
    for x in range(n):
        high = max(high, highs[x][0] + highs[x][1] - w[x])
    
    return high