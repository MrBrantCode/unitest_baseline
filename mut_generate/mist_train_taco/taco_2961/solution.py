"""
QUESTION:
Boboniu has a directed graph with n vertices and m edges.

The out-degree of each vertex is at most k.

Each edge has an integer weight between 1 and m. No two edges have equal weights.

Boboniu likes to walk on the graph with some specific rules, which is represented by a tuple (c_1,c_2,…,c_k). If he now stands on a vertex u with out-degree i, then he will go to the next vertex by the edge with the c_i-th (1≤ c_i≤ i) smallest weight among all edges outgoing from u.

Now Boboniu asks you to calculate the number of tuples (c_1,c_2,…,c_k) such that

  * 1≤ c_i≤ i for all i (1≤ i≤ k). 
  * Starting from any vertex u, it is possible to go back to u in finite time by walking on the graph under the described rules. 

Input

The first line contains three integers n, m and k (2≤ n≤ 2⋅ 10^5, 2≤ m≤ min(2⋅ 10^5,n(n-1) ), 1≤ k≤ 9).

Each of the next m lines contains three integers u, v and w (1≤ u,v≤ n,u≠ v,1≤ w≤ m), denoting an edge from u to v with weight w. It is guaranteed that there are no self-loops or multiple edges and each vertex has at least one edge starting from itself.

It is guaranteed that the out-degree of each vertex is at most k and no two edges have equal weight.

Output

Print one integer: the number of tuples.

Examples

Input


4 6 3
4 2 1
1 2 2
2 4 3
4 1 4
4 3 5
3 1 6


Output


2


Input


5 5 1
1 4 1
5 1 2
2 5 3
4 3 4
3 2 5


Output


1


Input


6 13 4
3 5 1
2 5 2
6 3 3
1 4 4
2 6 5
5 3 6
4 1 7
4 3 8
5 2 9
4 2 10
2 1 11
6 1 12
4 6 13


Output


1

Note

For the first example, there are two tuples: (1,1,3) and (1,2,3). The blue edges in the picture denote the c_i-th smallest edges for each vertex, which Boboniu chooses to go through.

<image>

For the third example, there's only one tuple: (1,2,2,2).

<image>

The out-degree of vertex u means the number of edges outgoing from u.
"""

from random import randrange

def count_valid_tuples(n, m, k, edges):
    LIMIT = (1 << 31) - 1
    OFFSET = 10 ** 6
    
    # Initialize graph and hashes
    graph = [[] for _ in range(n)]
    hashes = [randrange(0, LIMIT + 1) for _ in range(n)]
    
    # Populate the graph with edges
    for (u, v, cost) in edges:
        u -= 1
        v -= 1
        graph[u].append(cost * OFFSET + v)
    
    # Initialize zobrist hashing arrays
    zob = [[0] * k for _ in range(k)]
    zob_all = 0
    
    # Calculate zobrist hash for all vertices
    for i in range(n):
        zob_all ^= hashes[i]
    
    # Calculate zobrist hash for each edge
    for v in range(n):
        deg = len(graph[v])
        graph[v] = sorted(graph[v])
        for (i, tmp) in enumerate(graph[v]):
            nxt_v = tmp % OFFSET
            zob[deg - 1][i] ^= hashes[nxt_v]
    
    # Recursive function to solve the problem
    def solve(digit, res):
        ans = 0
        if digit == k:
            return int(res == zob_all)
        for i in range(digit + 1):
            ans += solve(digit + 1, res ^ zob[digit][i])
        return ans
    
    # Start the recursive solving process
    return solve(0, 0)