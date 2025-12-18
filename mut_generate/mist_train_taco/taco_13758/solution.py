"""
QUESTION:
The clique problem is one of the most well-known NP-complete problems. Under some simplification it can be formulated as follows. Consider an undirected graph G. It is required to find a subset of vertices C of the maximum size such that any two of them are connected by an edge in graph G. Sounds simple, doesn't it? Nobody yet knows an algorithm that finds a solution to this problem in polynomial time of the size of the graph. However, as with many other NP-complete problems, the clique problem is easier if you consider a specific type of a graph.

Consider n distinct points on a line. Let the i-th point have the coordinate x_{i} and weight w_{i}. Let's form graph G, whose vertices are these points and edges connect exactly the pairs of points (i, j), such that the distance between them is not less than the sum of their weights, or more formally: |x_{i} - x_{j}| ≥ w_{i} + w_{j}.

Find the size of the maximum clique in such graph.


-----Input-----

The first line contains the integer n (1 ≤ n ≤ 200 000) — the number of points.

Each of the next n lines contains two numbers x_{i}, w_{i} (0 ≤ x_{i} ≤ 10^9, 1 ≤ w_{i} ≤ 10^9) — the coordinate and the weight of a point. All x_{i} are different.


-----Output-----

Print a single number — the number of vertexes in the maximum clique of the given graph.


-----Examples-----
Input
4
2 3
3 1
6 1
0 2

Output
3



-----Note-----

If you happen to know how to solve this problem without using the specific properties of the graph formulated in the problem statement, then you are able to get a prize of one million dollars!

The picture for the sample test. [Image]
"""

def find_max_clique_size(n, points):
    """
    Finds the size of the maximum clique in a graph formed by n points on a line,
    where an edge exists between two points if the distance between them is not less
    than the sum of their weights.

    Parameters:
    n (int): The number of points.
    points (list of tuples): A list of tuples where each tuple contains the coordinate
                             x_i and the weight w_i of a point.

    Returns:
    int: The size of the maximum clique in the graph.
    """
    if n == 0:
        return 0
    
    # Sort points by their coordinates
    points.sort()
    
    # Initialize variables
    max_clique_size = 1
    (ta, tb) = (points[0][0], points[0][1])
    
    # Iterate through the points to find the maximum clique size
    for i in range(1, n):
        if points[i][0] - points[i][1] >= ta + tb:
            max_clique_size += 1
            ta = points[i][0]
            tb = points[i][1]
        elif points[i][0] + points[i][1] < ta + tb:
            ta = points[i][0]
            tb = points[i][1]
    
    return max_clique_size