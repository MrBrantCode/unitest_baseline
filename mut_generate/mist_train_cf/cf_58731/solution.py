"""
QUESTION:
Create a function `tsp` to solve the Traveling Salesman Problem using the Held-Karp algorithm. The function should take a weighted adjacency matrix `dist` of size `n x n` as input, where `n` is the number of cities, and `dist[i][j]` represents the cost of travel from city `i` to city `j`. The function should return the minimum cost for the salesman to visit all cities and return to the starting city. The function should assume that the weight between a city and itself is 0, and the weight between two cities is the same in both directions.
"""

def tsp(dist):
    """
    Solves the Traveling Salesman Problem using the Held-Karp algorithm.

    Args:
    dist (list of lists): A weighted adjacency matrix of size n x n, where n is the number of cities.
    
    Returns:
    The minimum cost for the salesman to visit all cities and return to the starting city.
    """

    n = len(dist)
    memo = [[[float('inf')] * (1 << n) for _ in range(n)] for _ in range(n)]

    for a in range(n):
        for b in range(n):
            memo[a][b][1 << b] = dist[a][b]

    for subset in range(1, 1 << n):
        for a in range(n):
            for b in range(n):
                if ((subset >> b) & 1) == 0:
                    continue
                for c in range(n):
                    if a == c or ((subset >> c) & 1) == 0:
                        continue
                    subset_without_b = subset ^ (1 << b)
                    memo[a][b][subset] = min(memo[a][b][subset], memo[a][c][subset_without_b] + dist[c][b])

    result = float('inf')
    for a in range(1, n):
        result = min(result, memo[a][0][(1 << n) - 1] + dist[a][0])

    return result