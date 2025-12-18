"""
QUESTION:
Graph constructive problems are back! This time the graph you are asked to build should match the following properties.

The graph is connected if and only if there exists a path between every pair of vertices.

The diameter (aka "longest shortest path") of a connected undirected graph is the maximum number of edges in the shortest path between any pair of its vertices.

The degree of a vertex is the number of edges incident to it.

Given a sequence of $n$ integers $a_1, a_2, \dots, a_n$ construct a connected undirected graph of $n$ vertices such that:  the graph contains no self-loops and no multiple edges;  the degree $d_i$ of the $i$-th vertex doesn't exceed $a_i$ (i.e. $d_i \le a_i$);  the diameter of the graph is maximum possible. 

Output the resulting graph or report that no solution exists.


-----Input-----

The first line contains a single integer $n$ ($3 \le n \le 500$) — the number of vertices in the graph.

The second line contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le n - 1$) — the upper limits to vertex degrees.


-----Output-----

Print "NO" if no graph can be constructed under the given conditions.

Otherwise print "YES" and the diameter of the resulting graph in the first line.

The second line should contain a single integer $m$ — the number of edges in the resulting graph.

The $i$-th of the next $m$ lines should contain two integers $v_i, u_i$ ($1 \le v_i, u_i \le n$, $v_i \neq u_i$) — the description of the $i$-th edge. The graph should contain no multiple edges — for each pair $(x, y)$ you output, you should output no more pairs $(x, y)$ or $(y, x)$.


-----Examples-----
Input
3
2 2 2

Output
YES 2
2
1 2
2 3

Input
5
1 4 1 1 1

Output
YES 2
4
1 2
3 2
4 2
5 2

Input
3
1 1 1

Output
NO



-----Note-----

Here are the graphs for the first two example cases. Both have diameter of $2$. [Image] $d_1 = 1 \le a_1 = 2$

$d_2 = 2 \le a_2 = 2$

$d_3 = 1 \le a_3 = 2$  [Image] $d_1 = 1 \le a_1 = 1$

$d_2 = 4 \le a_2 = 4$

$d_3 = 1 \le a_3 = 1$

$d_4 = 1 \le a_4 = 1$
"""

def construct_max_diameter_graph(n, a):
    x = []
    y = []
    for i in range(n):
        if a[i] == 1:
            y.append(i + 1)
        else:
            x.append([a[i], i + 1])
    
    if len(x) == 0 and n > 2:
        return "NO", None, None
    
    e = []
    for i in range(1, len(x)):
        e.append((x[i - 1][1], x[i][1]))
    
    if len(x) >= 2:
        x[0][0] -= 1
        x[-1][0] -= 1
        for i in range(1, len(x) - 1):
            x[i][0] -= 2
    
    d = len(e)
    yp = 0
    
    if x[0][0] > 0:
        if yp < len(y):
            e.append((x[0][1], y[yp]))
            x[0][0] -= 1
            yp += 1
            d += 1
        if len(x) == 1:
            if x[0][0] > 0:
                if yp < len(y):
                    e.append((x[0][1], y[yp]))
                    x[0][0] -= 1
                    yp += 1
                    d += 1
    
    if len(x) > 1 and x[-1][0] > 0:
        if yp < len(y):
            e.append((x[-1][1], y[yp]))
            x[-1][0] -= 1
            yp += 1
            d += 1
    
    for i in range(len(x)):
        while x[i][0] > 0 and yp < len(y):
            e.append((x[i][1], y[yp]))
            yp += 1
            x[i][0] -= 1
    
    if yp < len(y):
        return "NO", None, None
    
    return "YES", d, e