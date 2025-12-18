"""
QUESTION:
Write a function named `find_optimal_route(fuel, distance, time, storm_factor)` that takes four lists as input, where `fuel` is the amount of fuel needed to travel each segment without a solar storm, `distance` is the distance of each segment, `time` is the time it takes to travel each segment without a solar storm, and `storm_factor` is the factor by which travel time is increased due to the solar storm. The function should return a tuple containing the minimum amount of fuel needed for the entire journey and the total distance covered. Assume that the input lists are of the same length. The function should use dynamic programming to find the most fuel-efficient route while considering the effects of the solar storm on travel time and fuel usage.
"""

def entrance(fuel, distance, time, storm_factor):
    n = len(distance)
    f = [[0] * n for _ in range(n)]
    for j in range(n):
        f[0][j] = fuel[j]
    for i in range(1, n):
        for j in range(i, n):
            f[i][j] = float('inf')
            for k in range(j):
                f[i][j] = min(f[i][j], f[i-1][k] + fuel[j] + (distance[j]-distance[k]) * (storm_factor[k]+1) * fuel[j])
    return f[n-1][n-1], sum(distance)