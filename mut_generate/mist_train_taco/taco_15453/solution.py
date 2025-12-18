"""
QUESTION:
Sevenkplus has a rooted tree with $N$ vertices. The vertices are labeled from $1$ to $N$. $1$ is the root of the tree. Each vertex $v$ has a weight $W_v$. 

He forms a $N\times N$ matrix ${M}$ from the tree. ${M}$ is defined by 

$M(x,y)=W_{lca(x,y)}$ 

where $lca(x,y)$ is the lowest common ancestor of vertex ${x}$ and vertex $y$. 

He wants to calculate the determinant of ${M}$.  

Input Format 

First line contains the number of vertices, $N$. 

Second line contains $N$ numbers, $W_1\:W_2\:\cdots\:W_N$ separated by a space. 

This is followed by $N-1$ lines. Each line contains two numbers ${x}$, $y$, denoting that there is an edge between ${x}$  and $y$.  

Output Format 

Output one line, the determinant of ${M}$ modulo $(10^9+7)$.

Constraints 

$1\leq N\leq10^5$ 

$\forall i,0\leq W_i\leq10^9$. 

Sample Input

3
1 2 3
1 2
1 3

Sample Output

2

Explanation

$M=\begin{bmatrix}1&1&1\\ 1&2&1\\ 1&1&3\end{bmatrix}$

Then, $|M|=1\times\begin{bmatrix}2&1\\ 1&3\end{bmatrix}-1\times\begin{bmatrix}1&1\\ 1&3\end{bmatrix}+1\times\begin{bmatrix}1&2\\ 1&1\end{bmatrix}$. 

Hence $|M|=(1\times5)-(1\times2)+(1\times-1)=2$

Timelimits 

Timelimits for this challenge is given here
"""

import collections

MOD = 1000000007

def compute_matrix_determinant(N, weights, edges):
    # Build the tree structure
    tree = collections.defaultdict(set)
    for (x, y) in edges:
        tree[x].add(y)
        tree[y].add(x)
    
    # Function to compute the determinant using DFS
    def dfs_compute(tree, weights, root):
        visited = set()
        stack = [(-1, root)]
        product = 1
        while stack:
            (parent, node) = stack.pop()
            if node not in visited:
                visited.add(node)
                product *= weights[node - 1] - (weights[parent - 1] if parent > -1 else 0)
                product %= MOD
                for child in tree[node] - visited:
                    stack.append((node, child))
        return product
    
    # Compute the determinant starting from the root (vertex 1)
    return dfs_compute(tree, weights, 1)