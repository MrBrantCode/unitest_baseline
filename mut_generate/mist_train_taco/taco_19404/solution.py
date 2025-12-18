"""
QUESTION:
You are given $\textit{q}$ queries where each query consists of a set of $n$ points on a two-dimensional plane (i.e., $(x,y)$). For each set of points, print YES on a new line if all the points fall on the edges (i.e., sides and/or corners) of a non-degenerate rectangle which is axis parallel; otherwise, print NO instead. 

Input Format

The first line contains a single positive integer, $\textit{q}$, denoting the number of queries. The subsequent lines describe each query in the following format:

The first line contains a single positive integer, $n$, denoting the number of points in the query.      
Each line $\boldsymbol{i}$ of the $n$ subsequent lines contains two space-separated integers describing the respective values of $x_i$ and $y_i$ for the point at coordinate $(x_i,y_i)$.

Constraints

$1\leq q\leq10$
$1\leq n\leq10$
$-10^4\leq x,y\leq10^4$

Output Format

For each query, print YES on a new line if all $n$ points lie on the edges of some non-degenerate rectangle which is axis parallel; otherwise, print NO instead. 

Sample Input
2
3
0 0
0 1
1 0
4
0 0
0 2
2 0
1 1

Sample Output
YES
NO

Explanation

We perform the following $q=2$ queries:

In the first query, all points lie on the edges of a non-degenerate rectangle with corners at $(0,0)$, $(0,1)$, $(1,0)$, and $(1,1)$. Thus, we print YES on a new line.
In the second query, points $(0,0)$, $(0,2)$, and $(2,0)$ could all lie along the edge of some non-degenerate rectangle, but point $(1,1)$ would have to fall inside that rectangle. Thus, we print NO on a new line.
"""

def check_points_on_rectangle_edges(points):
    if not points:
        return "NO"
    
    px, py = zip(*points)
    x0 = min(px)
    x1 = max(px)
    y0 = min(py)
    y1 = max(py)
    
    result = all((x in (x0, x1) or y in (y0, y1) for (x, y) in points))
    
    return "YES" if result else "NO"