"""
QUESTION:
A pair of nodes, $(a,b)$, is a similar pair if the following conditions are true:

node $a$ is the ancestor of node $b$
$abs(a-b)\leq k$

Given a tree where each node is labeled from $1$ to $n$, find the number of similar pairs in the tree.

For example, given the following tree:  

We have the following pairs of ancestors and dependents:  

Pair	abs(a-b)	Pair	abs(a-b)
1,2	1		3,4	1
1,3	2		3,5	2
1,4	3		3,6	3
1,5	4
1,6	5

If $k=3$ for example, we have $6$ pairs that are similar, where $abs(a-b)\leq k$.

Function Description

Complete the similarPair function in the editor below.  It should return an integer that represents the number of pairs meeting the criteria.

similarPair has the following parameter(s):  

n: an integer that represents the number of nodes  
k: an integer
edges: a two dimensional array where each element consists of two integers that represent connected node numbers  

Input Format

The first line contains two space-separated integers $n$ and $k$, the number of nodes and the similarity threshold. 

Each of the next $n-1$ lines contains two space-separated integers defining an edge connecting nodes $p[i]$ and $c[i]$, where node $p[i]$ is the parent to node $c[i]$.

Constraints

$1\leq n\leq10^5$  
$0\leq k\leq n$  
$1\leq p[i],c[i]\leq n$  

Output Format

Print a single integer denoting the number of similar pairs in the tree.

Sample Input
5 2
3 2
3 1
1 4
1 5

Sample Output
4

Explanation

The similar pairs are $(3,2)$, $(3,1)$, $(3,4)$, and $(3,5)$, so we print $4$ as our answer. 

Observe that $(1,4)$ and $(1,5)$ are not similar pairs because they do not satisfy $abs(a-b)\leq k$ for $k=2$.
"""

def count_similar_pairs(n, k, edges):
    # Initialize the graph and matrix
    graph = [[] for _ in range(n)]
    matrix = [i for i in range(n)]
    
    # Build the graph and update the matrix
    for a, b in edges:
        matrix[b - 1] = a - 1
        graph[a - 1].append(b - 1)
    
    # Find the root of the tree
    p = 0
    while matrix[p] != p:
        p = matrix[p]
    
    # Initialize variables for DFS traversal
    total = 0
    stack = [p]
    path = []
    
    # Perform DFS to count similar pairs
    while stack:
        n = stack.pop()
        if isinstance(n, tuple):
            path.pop(n[0])
            continue
        
        total += bisect.bisect_right(path, n + k) - bisect.bisect_left(path, n - k)
        
        if not graph[n]:
            continue
        
        i = bisect.bisect_left(path, n)
        path.insert(i, n)
        stack.append((i,))
        stack.extend(graph[n])
    
    return total