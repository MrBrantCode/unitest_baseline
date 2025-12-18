"""
QUESTION:
Recall that a tree is an undirected, connected acyclic graph. We have a weighted tree, $\mathbf{T}$, with $n$ vertices; let $dist_{u,v}$ be the total sum of edge weights on the path between nodes $\mbox{u}$ and $\boldsymbol{\nu}$.

Let's consider all the matrices, $A_{u,v}$, such that:

$A_{u,v}=-A_{v,u}$
$0\leq|A_{u,v}|\leq dist_{u,v}$
$\sum_{i=1}^{n}A_{u,i}=0$ for each $u\neq1$ and $u\neq n$

We consider the total value of matrix $\mbox{A}$ to be:
$\sum_{i=1}^{n}A_{1,i}$

Calculate and print the maximum total value of $\mbox{A}$ for a given tree, $\mathbf{T}$.

Input Format

The first line contains a single positive integer, $n$, denoting the number of vertices in tree $\mathbf{T}$. 

Each line $\boldsymbol{i}$ of the $n-1$ subsequent lines contains three space-separated positive integers denoting the respective $a_i$, $b_i$, and $c_i$ values defining an edge connecting nodes $a_i$ and $b_i$ (where $1\leq a_i,b_i\leq n$) with edge weight $c_i$.

Constraints

$2\leq n\leq5000000$
$1\leq c_i\leq10^4$
Test cases with $n\leq10$ have $30\%$ of total score
Test cases with $n\leq500$ have $60\%$ of total score 

Output Format

Print a single integer denoting the maximum total value of matrix $\mbox{A}$ satisfying the properties specified in the Problem Statement above.

Sample Input
3
1 2 2
1 3 1

Sample Output
3

Explanation

In the sample case, matrix $\mbox{A}$ is:

$A=\begin{pmatrix}0&2&1\\ -2&0&2\\ -1&-2&0\end{pmatrix}$

The sum of the elements of the first row is equal to $3$.
"""

def calculate_max_total_value(n, edges):
    def dfs(graph, start, dlength, EdgeDis):
        (visited, stack) = (set(), [start])
        distances = [-1] * dlength
        distances[int(start) - 1] = 0
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                for v in graph[vertex]:
                    if distances[int(v) - 1] == -1:
                        distances[int(v) - 1] = distances[int(vertex) - 1] + min(EdgeDis[tuple([vertex, v])])
                stack.extend(graph[vertex] - visited)
        return [x for x in distances if x != -1]

    graph = dict()
    EdgeDis = dict()
    for (a, b, c) in edges:
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)
        EdgeDis.setdefault(tuple([a, b]), list()).append(c)
        EdgeDis.setdefault(tuple([b, a]), list()).append(c)

    sol = dfs(graph, 1, n, EdgeDis)
    sol2 = dfs(graph, n, n, EdgeDis)
    
    return min(sum(sol), sum(sol2))