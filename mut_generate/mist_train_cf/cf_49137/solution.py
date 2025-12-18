"""
QUESTION:
You are given two groups of points where the first group has `size1` points and the second group has `size2` points, with `size1 >= size2`. The cost of connecting any two points is given in an `size1 x size2` matrix where `cost[i][j]` is the cost of connecting point `i` of the first group and point `j` of the second group. Each point in the first group can only be connected to a maximum of `k` points in the second group, and each point in the second group can only be connected to a maximum of `k` points in the first group.

Write a function `connectTwoGroups(cost, k)` to return the minimum cost it takes to connect the two groups under these constraints. The input `cost` is a 2D array of integers and `k` is an integer. The constraints are `1 <= size1, size2 <= 12`, `size1 >= size2`, `0 <= cost[i][j] <= 100`, and `1 <= k <= size1`.
"""

def connectTwoGroups(cost, k): 
    size1, size2 = len(cost), len(cost[0]) 
    min_cost = [min(cost[j][i] for j in range(size1)) for i in range(size2)] 
    dp = [[float('inf')]*(1<<size2) for _ in range(size1)] 

    def dfs(point, mask): 
        if point == -1: 
            return sum(i for i in range(size2) if (mask & 1<<i) == 0 for i in min_cost) 
        elif dp[point][mask] != float('inf'): 
            return dp[point][mask] 
        else: 
            for i in range(size2): 
                dp[point][mask] = min(dp[point][mask], cost[point][i] + dfs(point-1, mask|1<<i)) 
            return dp[point][mask] 

    res = dfs(size1-1, 0)
    return res