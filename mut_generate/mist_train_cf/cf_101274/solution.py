"""
QUESTION:
Write a function `find_optimal_route(fuel, distance, storm_factor)` that calculates the minimum fuel required to travel from Earth to the Moon and the total distance covered, given the fuel required for each segment, the distance of each segment, and the factor by which travel time is increased due to the solar storm for each segment. The function should assume that the input lists are of the same length and represent the values for each segment of the journey. The function should return a tuple containing the minimum fuel required and the total distance covered. The fuel required for each segment should be calculated based on the minimum fuel needed to travel the previous segments plus the fuel needed to travel the current segment with the solar storm factor taken into account.
"""

def find_optimal_route(fuel, distance, storm_factor):
    n = len(distance)
    f = [[0] * n for _ in range(n)]
    for j in range(n):
        f[0][j] = fuel[j]
    for i in range(1, n):
        for j in range(i+1, n):
            f[i][j] = float('inf')
            for k in range(j):
                f[i][j] = min(f[i][j], f[i-1][k] + fuel[j] + (distance[j]-distance[k]) * (storm_factor[k]+1) * fuel[j])
    return f[n-1][n-1], sum(distance)