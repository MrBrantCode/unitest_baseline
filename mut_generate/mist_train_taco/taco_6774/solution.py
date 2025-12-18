"""
QUESTION:
Given a directed weighted graph where weight indicates distance, for each query, determine the length of the shortest path between nodes.  There may be many queries, so efficiency counts.  

For example, your graph consists of $5$ nodes as in the following:

A few queries are from node $4$ to node $3$, node $2$ to node $5$, and node $5$ to node $3$. 

There are two paths from $4$ to $3$:

$4\Rightarrow1\Rightarrow2\Rightarrow3$ at a distance of $4+5+1=10$  
$4\Rightarrow1\Rightarrow5\Rightarrow3$ at a distance of $4+3+2=9$ 

In this case we choose path $2$.  

There is no path from $2$ to $5$, so we return $-1$.  

There is one path from $5$ to $3$:  

$5\Rightarrow3$ at a distance of $2$.  

Input Format

The first line has two integers $n$ and $m$, the number of nodes and the number of edges in the graph. 

Each of the next $m$ lines contains three space-separated integers $\mbox{u}$ $v$ and $\boldsymbol{w}$, the two nodes between which the directed edge $u\Rightarrow v$ exists, and $\boldsymbol{w}$, the length of the edge. 

The next line contains a single integer $\textit{q}$, the number of queries. 

Each of the next $\textit{q}$ lines contains two space-separated integers $a$ and $\boldsymbol{b}$, denoting the start and end nodes for traversal.  

Constraints

$2\leq n\leq400$ 

$1\leq m\leq\frac{n\times(n-1)}{2}$ 

$1\leq q\leq10^5$ 

$1\leq u,v\leq n$ 

$1\leq w\leq350$ 

The distance from a node to itself is always $0$ and it is always reachable from itself.

If there are edges between the same pair of nodes with different weights, the last one (most recent) is to be considered as the only edge between them.

Output Format

Print $\textit{q}$ lines, each containing a single integer specifying the shortest distance for the query.  

If the destination node is not reachable, return $-1$.  

Sample Input
STDIN   Function
-----   --------
4 5     n = 4, m = 5
1 2 5   u = 1, v = 2, w = 5
1 4 24  u = 1, v =4, w = 24 ...
2 4 6
3 4 4
3 2 7
3       q = 3
1 2     query 0: from 1 to 2
3 1     query 1: from 3 to 1
1 4     query 2: from 1 to 4

Sample Output
5
-1
11

Explanation

The graph given in the test case is:

The shortest paths for the 3 queries are :

$1\Rightarrow2$: The direct path is shortest with weight 5  
$-1$: There is no way of reaching node 1 from node 3  
$1\Rightarrow2\Rightarrow4$: The indirect path is shortest with weight (5+6) = 11 units. The direct path is longer with 24 units length.
"""

def shortest_path_queries(n, m, edges, queries):
    INFINITY = 4294967295

    class Vertex:
        def __init__(self):
            self.adj = {}

    def bellman_ford(V, s, sp):
        sp[s][s] = 0
        sps = sp[s]
        for i in range(n):
            done = True
            for x in range(n):
                for y in V[x].adj.keys():
                    w = V[x].adj[y]
                    if sps[y] > sps[x] + w:
                        sps[y] = sps[x] + w
                        done = False
            if done:
                break

    # Initialize vertices and shortest path matrix
    V = [Vertex() for _ in range(n)]
    SP = [[INFINITY for _ in range(n)] for _ in range(n)]

    # Populate the graph with edges
    for (u, v, w) in edges:
        V[u - 1].adj[v - 1] = w

    # Process each query
    results = []
    for (a, b) in queries:
        a -= 1
        b -= 1
        if SP[a][a] == INFINITY:
            bellman_ford(V, a, SP)
        if SP[a][b] == INFINITY:
            results.append(-1)
        else:
            results.append(SP[a][b])

    return results