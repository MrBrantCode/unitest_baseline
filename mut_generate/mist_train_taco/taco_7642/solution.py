"""
QUESTION:
Read problems statements in [Hindi], [Mandarin Chinese], [Russian], [Vietnamese], and [Bengali] as well.

In a *red-blue tree*, each vertex is either red or blue and adjacent vertices always have different colours.

You are given a tree with $N$ vertices (numbered $1$ through $N$). It is not necessarily a red-blue tree, but its vertices are still coloured red and blue. You may perform the following operation any number of times (including zero): choose two adjacent vertices and swap their colours.

Find the smallest number of operations required to transform the tree into a red-blue tree or determine that it is impossible.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains a single integer $N$.
$N-1$ lines follow. Each of these lines contains two space-separated integers $u$ and $v$ denoting that vertices $u$ and $v$ are connected by an edge.
The last line contains a string $S$ with length $N$. For each valid $i$, the $i$-th character of this string is either '0' if the $i$-th vertex is initially red or '1' if it is initially blue.

------  Output ------
Print a single line containing one integer ― the smallest number of operations or $-1$ if it is impossible to transform the tree into a red-blue tree.

------  Constraints ------
$1 ≤ T ≤ 100$  
$1 ≤ N ≤ 100,000$  
$1 ≤ u, v ≤ N$  
$S$ contains only characters '0' and '1'
the sum of $N$ over all test cases does not exceed $10^{6}$

----- Sample Input 1 ------ 
1  

7  

1 2  

1 3  

2 4  

2 5  

3 6  

3 7  

0010010
----- Sample Output 1 ------ 
3
----- explanation 1 ------ 
Example case 1: We can perform the following operations:
- Swap the colours of vertices $1$ and $3$; the string of colours becomes "1000010".
- Swap the colours of vertices $1$ and $2$; the string of colours becomes "0100010".
- Swap the colours of vertices $6$ and $3$; the string of colours becomes "0110000", so the tree is a red-blue tree.
"""

def min_operations_to_red_blue_tree(N, edges, colors):
    def calc_colors(nodes, x, colors, exp_color, parent):
        total_value = 0
        total_value1 = 0
        if exp_color == '1':
            val = 1
            next_exp = '0'
        else:
            val = -1
            next_exp = '1'
        if colors[x] != exp_color:
            total_value = val
        else:
            total_value1 = val
        total_dist = 0
        total_dist1 = 0
        for i in nodes[x]:
            if i == parent:
                continue
            (dist, val, dist1, val1) = calc_colors(nodes, i, colors, next_exp, x)
            total_dist += dist
            total_value += val
            total_dist1 += dist1
            total_value1 += val1
        total_dist += abs(total_value)
        total_dist1 += abs(total_value1)
        return (total_dist, total_value, total_dist1, total_value1)

    # Build the adjacency list
    nodes = [[] for _ in range(N)]
    for u, v in edges:
        nodes[u - 1].append(v - 1)
        nodes[v - 1].append(u - 1)

    # Calculate the minimum operations
    (dist1, val1, dist2, val2) = calc_colors(nodes, 0, colors, '0', 0)
    if val1 != 0 != val2:
        return -1
    elif val1 == 0 == val2:
        return min(dist1, dist2)
    elif val1 == 0:
        return dist1
    else:
        return dist2