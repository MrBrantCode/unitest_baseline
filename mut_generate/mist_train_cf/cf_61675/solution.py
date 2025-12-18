"""
QUESTION:
Develop an algorithm for the function `held_karp_tsp` that takes a 2D distance matrix as input, where `distance_matrix[i][j]` represents the distance from city `i` to city `j`, and returns the minimum cost (shortest distance) of a circular tour that visits all cities exactly once and returns to the starting city. Assume the distance matrix is a square matrix with `n` rows and `n` columns, where `n` is the number of cities, and all distances are non-negative.
"""

def held_karp_tsp(distance_matrix):
    """
    Returns the minimum cost (shortest distance) of a circular tour that visits all cities exactly once and returns to the starting city.
    
    Args:
    distance_matrix (list of lists): A 2D distance matrix where distance_matrix[i][j] represents the distance from city i to city j.
    
    Returns:
    int: The minimum cost of the tour.
    """
    
    n = len(distance_matrix)
    dp = [[[float('inf')] * n for _ in range(1 << n)] for _ in range(n)]
    
    # Initialize base case where salesman only visits the given city
    for i in range(n):
        dp[i][1 << i][i] = 0
    
    # Compute minimum cost path for every subset of cities
    for mask in range(1, 1 << n):
        for node in range(n):
            if not (mask & (1 << node)):
                continue
            for node2 in range(n):
                if node == node2:
                    continue
                if (mask & (1 << node2)) == 0:
                    continue
                new_mask = mask ^ (1 << node)
                dp[node][mask][node2] = min(dp[node][mask][node2], dp[node2][new_mask][node] + distance_matrix[node2][node])
    
    # Find minimum cost amongst all tours that visit every city and end at the source city
    min_cost = float('inf')
    for node in range(1, n):
        min_cost = min(min_cost, dp[node][(1 << n) - 1][0] + distance_matrix[0][node])
    
    return min_cost + distance_matrix[0][0]