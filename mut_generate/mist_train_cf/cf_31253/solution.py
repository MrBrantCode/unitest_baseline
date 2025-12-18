"""
QUESTION:
Implement a function `maximize_load(weights, capacity)` that maximizes the total weight of items that can be loaded onto a truck without exceeding its capacity. The function takes a list of weights and the truck's weight capacity as input, and returns the maximum total weight that can be loaded onto the truck. Each item can only be loaded once and in whole.
"""

from typing import List

def maximize_load(weights: List[int], capacity: int) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], weights[i - 1] + dp[i - 1][w - weights[i - 1]])

    return dp[n][capacity]