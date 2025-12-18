"""
QUESTION:
A clique in a graph is set of nodes such that there is an edge between any two distinct nodes in the set. Finding the largest clique in a graph is a computationally difficult problem. Currently no polynomial time algorithm  is known for solving this. However, you wonder what is the minimum size of the largest clique in any graph with $n$ nodes and $m$ edges.  

For example, consider a graph with $n=4$ nodes and $m=5$ edges.  The graph below shows $4$ nodes with $4$ edges and no cliques.  It is evident that the addition of any $5^{th}$ edge must create two cliques with $3$ members each.  

Input Format

The first line contains an integer $\boldsymbol{\boldsymbol{t}}$, the number of test cases.  

Each of the next $\boldsymbol{\boldsymbol{t}}$ lines contains two space-separated integers $n$ and $m$.  

Constraints

$1\leq t\leq100000$  
$2\leq n\leq10000$  
$1\leq m\leq\frac{n\times(n-1)}{2}$

Output Format

For each test case, print the minimum size of the largest clique that must be formed given $n$ and $m$.   

Sample Input
3  
3 2  
4 6  
5 7

Sample Output
2  
4  
3

Explanation

For the first case, we have two cliques with two nodes each:  

For the second test case, the only valid graph having $4$ nodes and $\boldsymbol{6}$ edges is one where each pair of nodes is connected. So the size of the largest clique cannot be smaller than $4$.  

For the third test case, it is easy to verify that any graph with $5$ nodes and $7$.  The $5$ solid lines in the graph below indicate the maximum edges that can be added without forming a clique larger than $2$.  The dashed lines could connect any two nodes not connected by solid lines producing a clique of size $3$.  

Hints 
Turan's theorem gives us an upper bound on the number of edges a graph can have if we wish that it should not have a clique of size $\boldsymbol{x}$. Though the bound is not exact, it is easy to extend the statement of the theorem to get an exact bound in terms of $n$ and $\boldsymbol{x}$. Once this is done, we can binary search for the largest $\boldsymbol{x}$ such that $f(n,x)<=m$. See: Turan's Theorem
"""

def minimum_largest_clique_size(n: int, m: int) -> int:
    """
    Calculate the minimum size of the largest clique in a graph with `n` nodes and `m` edges.

    Parameters:
    n (int): The number of nodes in the graph.
    m (int): The number of edges in the graph.

    Returns:
    int: The minimum size of the largest clique.
    """
    def s1(n, m):
        ga = n % m
        gb = m - ga
        sa = n // m + 1
        sb = n // m
        return ga * gb * sa * sb + ga * (ga - 1) * sa * sa // 2 + gb * (gb - 1) * sb * sb // 2

    def s(n, c):
        l = 1
        h = n + 1
        while l + 1 < h:
            m = l + (h - l) // 2
            k = s1(n, m)
            if k < c:
                l = m
            else:
                h = m
        return h

    return s(n, m)