"""
QUESTION:
You are given a tree consisting of $n$ vertices. A tree is an undirected connected acyclic graph. [Image] Example of a tree. 

You have to paint each vertex into one of three colors. For each vertex, you know the cost of painting it in every color.

You have to paint the vertices so that any path consisting of exactly three distinct vertices does not contain any vertices with equal colors. In other words, let's consider all triples $(x, y, z)$ such that $x \neq y, y \neq z, x \neq z$, $x$ is connected by an edge with $y$, and $y$ is connected by an edge with $z$. The colours of $x$, $y$ and $z$ should be pairwise distinct. Let's call a painting which meets this condition good.

You have to calculate the minimum cost of a good painting and find one of the optimal paintings. If there is no good painting, report about it.


-----Input-----

The first line contains one integer $n$ $(3 \le n \le 100\,000)$ — the number of vertices.

The second line contains a sequence of integers $c_{1, 1}, c_{1, 2}, \dots, c_{1, n}$ $(1 \le c_{1, i} \le 10^{9})$, where $c_{1, i}$ is the cost of painting the $i$-th vertex into the first color.

The third line contains a sequence of integers $c_{2, 1}, c_{2, 2}, \dots, c_{2, n}$ $(1 \le c_{2, i} \le 10^{9})$, where $c_{2, i}$ is the cost of painting the $i$-th vertex into the second color.

The fourth line contains a sequence of integers $c_{3, 1}, c_{3, 2}, \dots, c_{3, n}$ $(1 \le c_{3, i} \le 10^{9})$, where $c_{3, i}$ is the cost of painting the $i$-th vertex into the third color.

Then $(n - 1)$ lines follow, each containing two integers $u_j$ and $v_j$ $(1 \le u_j, v_j \le n, u_j \neq v_j)$ — the numbers of vertices connected by the $j$-th undirected edge. It is guaranteed that these edges denote a tree.


-----Output-----

If there is no good painting, print $-1$.

Otherwise, print the minimum cost of a good painting in the first line. In the second line print $n$ integers $b_1, b_2, \dots, b_n$ $(1 \le b_i \le 3)$, where the $i$-th integer should denote the color of the $i$-th vertex. If there are multiple good paintings with minimum cost, print any of them.


-----Examples-----
Input
3
3 2 3
4 3 2
3 1 3
1 2
2 3

Output
6
1 3 2 

Input
5
3 4 2 1 2
4 2 1 5 4
5 3 2 1 1
1 2
3 2
4 3
5 3

Output
-1

Input
5
3 4 2 1 2
4 2 1 5 4
5 3 2 1 1
1 2
3 2
4 3
5 4

Output
9
1 3 2 1 3 



-----Note-----

All vertices should be painted in different colors in the first example. The optimal way to do it is to paint the first vertex into color $1$, the second vertex — into color $3$, and the third vertex — into color $2$. The cost of this painting is $3 + 2 + 1 = 6$.
"""

def find_min_cost_painting(n, c1, c2, c3, edges):
    from itertools import chain
    
    # Initialize the tree structure
    tree = [[] for _ in range(n)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    # Check if any vertex has more than 2 neighbors
    for u in range(n):
        if len(tree[u]) > 2:
            return -1
    
    # Find a leaf vertex to start the traversal
    for u in range(n):
        if len(tree[u]) == 1:
            v = u
            break
    
    # Initialize variables for traversal and cost calculation
    ans = [0] * n
    cost = [[0, 0, 0] for _ in range(4)]
    w = 0
    ansi = 1
    
    # Traverse the tree and calculate costs
    for _ in range(n):
        ans[v] = ansi
        cost[1][ansi] += c1[v]
        cost[2][ansi] += c2[v]
        cost[3][ansi] += c3[v]
        ansi = (ansi + 1) % 3
        if len(tree[v]) == 1:
            w = v
            (v,) = tree[v]
        else:
            (v, w) = (next((x for x in tree[v] if x != w)), v)
    
    # Find the minimum cost painting
    pal = min(((p1, p2, p3, cost[p1][0] + cost[p2][1] + cost[p3][2]) 
               for p1 in (1, 2, 3) 
               for p2 in (1, 2, 3) 
               if p1 != p2 
               for p3 in (6 - p1 - p2,)), key=lambda x: x[3])
    
    # Return the result
    if pal[3] == float('inf'):
        return -1
    else:
        return pal[3], [pal[ansi] for ansi in ans]