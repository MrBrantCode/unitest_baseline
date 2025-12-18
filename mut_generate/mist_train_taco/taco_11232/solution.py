"""
QUESTION:
You are given a table, $a$, with $n$ rows and $m$ columns. The top-left corner of the table has coordinates $(0,0)$, and the bottom-right corner has coordinates $(n-1,m-1)$. The $i^{\mbox{th}}$ cell contains integer $a_{i,j}$.

A path in the table is a sequence of cells $(r_1,c_1),(r_2,c_2),\ldots,(r_k,c_k)$ such that for each $i\in\{1,\ldots,k-1\}$, cell $(r_{i},c_{i})$ and cell $(r_{i+1},c_{i+1})$ share a side. 

The weight of the path $(r_1,c_1),(r_2,c_2),\ldots,(r_k,c_k)$ is defined by $\sum_{i=1}^{k}a_{r_{i},c_{i}}$ where $a_{r_i,c_i}$ is the weight of the cell $(r_{i},c_{i})$.

You must answer $q$ queries. In each query, you are given the coordinates of two cells, $(r_1,c_1)$ and $(r_2,c_2)$. You must find and print the minimum possible weight of a path connecting them.

Note: A cell can share sides with at most $4$ other cells. A cell with coordinates $(r,c)$ shares sides with $(r-1,c)$, $(r+1,c)$, $(r,c-1)$ and $(r,c+1)$.

Input Format

The first line contains $2$ space-separated integers, $n$ (the number of rows in $a$) and $m$ (the number of columns in $a$), respectively. 

Each of $n$ subsequent lines contains $m$ space-separated integers. The $j^{th}$ integer in the $i^{\mbox{th}}$ line denotes the value of $a_{i,j}$. 

The next line contains a single integer, $\textit{q}$, denoting the number of queries. 

Each of the $\textit{q}$ subsequent lines describes a query in the form of $A$ space-separated integers: $r_1$, $c_{1}$, $r_2$, and $c_2$, respectively. 

Constraints

$1\leq n\leq7$
$1\leq m\leq5\times10^3$
$0\leq a_{i,j}\leq3\times10^3$
$1\leq q\leq3\times10^4$

For each query:

$0\leq r_{1},r_{2}<n$
$0\leq c_1,c_2\lt m$

Output Format

On a new line for each query, print a single integer denoting the minimum possible weight of a path between $(r_1,c_1)$ and $(r_2,c_2)$.

Sample Input
3 5
0 0 0 0 0
1 9 9 9 1
0 0 0 0 0
3
0 0 2 4
0 3 2 3
1 1 1 3

Sample Output
1
1
18

Explanation

The input table looks like this:

The first two queries are explained below:

In the first query, we have to find the minimum possible weight of a path connecting $(0,0)$ and $(2,4)$. Here is one possible path:

The total weight of the path is $0+1+0+0+0+0+0=1$.

In the second query, we have to find the minimum possible weight of a path connecting $(0,3)$ and $(2,3)$. Here is one possible path:

The total weight of the path is $0+0+1+0+0=1$.
"""

def heuristic(board, r1, c1, r2, c2):
    return 0

def find_min_path_weight(board, r1, c1, r2, c2):
    open_nodes = {(r1, c1): (board[r1][c1], board[r1][c1] + heuristic(board, r1, c1, r2, c2))}
    closed_nodes = set()
    
    while open_nodes:
        (cur_est, cur_pos, cur_cost) = min(((est, pos, cost) for (pos, (cost, est)) in open_nodes.items()))
        del open_nodes[cur_pos]
        
        if cur_pos == (r2, c2):
            return cur_cost
        
        (r, c) = cur_pos
        neighbours = []
        if r > 0:
            neighbours.append((r - 1, c))
        if c > 0:
            neighbours.append((r, c - 1))
        if r < len(board) - 1:
            neighbours.append((r + 1, c))
        if c < len(board[0]) - 1:
            neighbours.append((r, c + 1))
        
        for nb_pos in neighbours:
            (r, c) = nb_pos
            cost = cur_cost + board[r][c]
            est = cost + heuristic(board, r, c, r2, c2)
            
            if nb_pos in closed_nodes:
                continue
            if nb_pos in open_nodes and open_nodes[nb_pos][0] <= cost:
                continue
            
            open_nodes[nb_pos] = (cost, est)
        
        closed_nodes.add(cur_pos)
    
    return -1  # In case no path is found, though the problem guarantees a path exists